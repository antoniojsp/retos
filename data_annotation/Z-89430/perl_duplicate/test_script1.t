use strict;
use warnings;

my $filename = "your_file.txt";
open(my $fh, '<', $filename) or die "Could not open file '$filename': $!";

my @lines = <$fh>;
my @sorted_unique = sort { $a cmp $b } @lines;

for (my $i = 1; $i < @sorted_unique; $i++) {
    print "Duplicate lin: $sorted_unique[$i]" if $sorted_unique[$i] eq $sorted_unique[$i - 1];
}

close $fh;