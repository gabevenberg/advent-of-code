const std = @import("std");

pub fn build(b: *std.Build) !void {
    const allocator = b.allocator;

    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const run_all = b.step("run", "Run all days");
    const test_all = b.step("test", "Test all days");
    const check = b.step("check", "run checks");

    const utils_mod = b.createModule(.{ .root_source_file = b.path("src/utils/mod.zig") });

    var dirIt = (try std.fs.cwd().openDir(
        "./src/days",
        .{ .iterate = true },
    )).iterate();

    while (try dirIt.next()) |entry| {
        if (entry.kind == .directory) {}
        // each day entry will have a main.zig
        const source_file = try std.fs.path.join(allocator, &.{ "src", "days", entry.name, "main.zig" });
        defer allocator.free(source_file);
        //make sure the main.zig exists
        _ = std.fs.cwd().openFile(source_file, .{}) catch continue;

        const exe = b.addExecutable(.{
            .name = entry.name,
            .root_source_file = b.path(source_file),
            .target = target,
            .optimize = optimize,
        });
        exe.root_module.addImport("utils", utils_mod);

        b.installArtifact(exe);
        const install_cmd = b.addInstallArtifact(exe, .{});
        const install_step = b.step(
            b.fmt("install_{s}", .{entry.name}),
            b.fmt("install {s}", .{entry.name}),
        );
        install_step.dependOn(&install_cmd.step);
        b.installArtifact(exe);

        const run_cmd = b.addRunArtifact(exe);
        const run_step = b.step(
            b.fmt("run_{s}", .{entry.name}),
            b.fmt("run {s}", .{entry.name}),
        );
        run_step.dependOn(&run_cmd.step);
        run_all.dependOn(&run_cmd.step);

        const exe_test = b.addTest(.{
            .root_source_file = b.path(source_file),
            .target = target,
            .optimize = optimize,
        });
        const test_cmd = b.addRunArtifact(exe_test);
        const test_step = b.step(
            b.fmt("test_{s}", .{entry.name}),
            b.fmt("test {s}", .{entry.name}),
        );
        test_step.dependOn(&test_cmd.step);
        test_all.dependOn(&test_cmd.step);

        const exe_check = b.addExecutable(.{
            .name = entry.name,
            .root_source_file = b.path(source_file),
            .target = target,
            .optimize = optimize,
        });
        exe_check.root_module.addImport("utils", utils_mod);
        check.dependOn(&exe_check.step);
    }
}
