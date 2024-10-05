# Import necessary PySpark libraries
from pyspark import SparkConf, SparkContext

# Initialize the Spark context
conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext(conf=conf)

# Step 1: Read the input file (Replace 'path/to/your/textfile.txt' with the actual file path)
text_file = sc.textFile("your_text_file.txt")

# Step 2: Mapper - Split lines into words, map each word to (word, 1)
words = text_file.flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1))

# Step 3: Reducer - Sum up the counts for each word
word_counts = words.reduceByKey(lambda a, b: a + b)

# Step 4: Collect and print the word counts
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Optionally: Save the output to a file
word_counts.saveAsTextFile("./out.txt")
