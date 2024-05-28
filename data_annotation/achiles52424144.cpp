#include <iostream>
#include <fstream>
#include <string>

void identifyComments(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    std::string line;
    bool inMultilineComment = false;

    while (std::getline(file, line)) {
        size_t pos = 0;

        // Check if we are currently inside a multi-line comment
        if (inMultilineComment) {
            size_t endPos = line.find("*/");
            if (endPos != std::string::npos) {
                // End of multi-line comment found
                std::cout << "Multi-line comment: " << line.substr(0, endPos + 2) << std::endl;
                inMultilineComment = false;
                pos = endPos + 2;
            } else {
                // Still inside multi-line comment
                std::cout << "Multi-line comment: " << line << std::endl;
                continue;
            }
        }
/* MARIA */
        while (pos < line.size()) {
            size_t singleLinePos = line.find("//", pos);
            size_t multiLineStartPos = line.find("/*", pos);

            if (singleLinePos == std::string::npos && multiLineStartPos == std::string::npos) {
                // No more comments in this line
                break;
            }

            if (singleLinePos != std::string::npos && (multiLineStartPos == std::string::npos || singleLinePos < multiLineStartPos)) {
                // Single-line comment found
                std::cout << "Single-line comment: " << line.substr(singleLinePos) << std::endl;
                break; // Rest of the line is a single-line comment
            }

            if (multiLineStartPos != std::string::npos) {
                // Multi-line comment start found
                size_t multiLineEndPos = line.find("*/", multiLineStartPos + 2);
                if (multiLineEndPos != std::string::npos) {
                    // Multi-line comment ends on the same line
                    std::cout << "Multi-line comment: " << line.substr(multiLineStartPos, multiLineEndPos - multiLineStartPos + 2) << std::endl;
                    pos = multiLineEndPos + 2;
                } else {
                    // Multi-line comment continues on the next lines
                    std::cout << "Multi-line comment: " << line.substr(multiLineStartPos) << std::endl;
                    inMultilineComment = true;
                    break;
                }
            }
        }
    }

    file.close();
}

int main() {
    std::string filename;
    std::cout << "Enter the filename: ";
    std::cin >> filename;

    identifyComments(filename);

    return 0;
}