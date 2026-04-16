const lib = @import("lib.zig");
const std = @import("std");
const utils = @import("utils");

pub fn solve(comptime input: []const u8) i32 {
    return input.len;
}

test "part2 sample" {
    const input =
        \\0
    ;
    try std.testing.expectEqual(solve(input), 1);
}
