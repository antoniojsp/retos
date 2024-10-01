use strict;
use warnings;

my $filename = "your_file.txt";
open(my $fh, '<', $filename) or die "Could not open file '$filename': $!";

my %seen;
while (my $line = <$fh>) {
    if ($seen{$line}) {
        print "Duplicate line: $line";  # Print duplicates as you find them
    } else {
        $seen{$line} = 1;
    }
}

close $fh;
            