const std = @import("std");
const part1 = @import("part1.zig");
const part2 = @import("part2.zig");
const input = @embedFile("input.txt");

pub fn main() !void {
    const stdout = std.io.getStdErr().writer();
    try stdout.print("Part1: {d}\n", .{part1.solve(input)});
    try stdout.print("Part2: {d}\n", .{part2.solve(input)});
}
