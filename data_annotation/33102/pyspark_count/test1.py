from pyspark import SparkContext, SparkConf


def mapper(line):
    """Map function that tokenizes the line and emits (word, 1) pairs."""
    words = line.split()
    return [(word, 1) for word in words]


def reducer(word, counts):
    """Reducer function that sums up the counts for each word."""
    return sum(counts)


if __name__ == "__main__":
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Replace "your_text_file.txt" with the actual path to your text file
    text_file = sc.textFile("your_text_file.txt")

    # Map the text file to (word, 1) pairs
    word_counts = text_file.flatMap(mapper).reduceByKey(reducer)

    # Collect the results and print them
    for word, count in word_counts.collect():
        print(f"{word}: {count}")

    sc.stop()
