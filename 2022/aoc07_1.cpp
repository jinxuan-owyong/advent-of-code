#include <ctype.h>

#include <iostream>
#include <sstream>
#include <stack>
#include <unordered_set>
#include <vector>

typedef std::vector<int> vi;
// To add an edge
void addEdge(std::vector<vi>& adj, int u, int v) {
    adj[u].emplace_back(v);
    adj[v].emplace_back(u);
}

class File {
private:
    int filesize = 0;

public:
    std::string name;
    File(std::string s, int sz) {
        name = s;
        filesize = sz;
    }
    int size() { return filesize; }
};

bool operator==(const File& lhs, const File& rhs) {
    return lhs.name == rhs.name;
}

template <>
struct std::hash<File> {
    std::size_t operator()(File const& f) const noexcept {
        return std::hash<std::string>{}(f.name);
    }
};

class Dir {
private:
    std::vector<Dir> dirs;
    std::unordered_set<File> files;
    int dirsize = 0;  // does not include subdirectories

public:
    std::string name;
    Dir* parent = NULL;
    Dir(std::string s) {
        name = s;
    }
    int size() { return dirsize; }
    void addFile(File f) {
        files.insert(f);
        dirsize += f.size();
    }
    Dir* find(std::string s) {
        for (int i = 0; i < dirs.size(); ++i) {
            if (dirs[i].name == s) {
                return &dirs[i];
            }
        }
        return NULL;  // directory does not exist
    }
    Dir* mkdir(std::string dirname) {
        Dir temp(dirname);
        temp.parent = this;
        dirs.emplace_back(temp);
        return &dirs[dirs.size() - 1];
    }
    void insertFile(std::string filename, int filesize) {
        files.insert(File(filename, filesize));
        dirsize += filesize;
    }
};

int main(void) {
    Dir root("/");
    Dir* cwd = &root;
    std::stack<std::string> curr;
    std::string line;
    while (std::getline(std::cin, line)) {
        std::istringstream iss(line);
        if (line[0] == '$') {
            std::string cmd;
            iss >> cmd >> cmd;  // discard $
            if (cmd == "cd") {
                std::string dirname;
                iss >> dirname;
                if (dirname == "..") {
                    curr.pop();
                    cwd = cwd->parent;
                } else {
                    curr.push(dirname);
                    cwd = cwd->mkdir(dirname);
                }
            } else {  // ls
            }
        } else if (std::isdigit(line[0])) {
            int size;
            std::string filename;
            iss >> size >> filename;
        } else {  // ls result
        }
        return 0;
    }