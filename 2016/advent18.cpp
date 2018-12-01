#include <iostream>
#include <ctime>
#include <string>
#include <vector>

void show(std::vector<bool> vec) {
    for(auto it = vec.begin(); it != vec.end(); ++it)
        std::cout << (*it);
    std::cout << std::endl;
}

int main(){
    std::string task("^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......");
    //std::string task("..^^.");
    int iterations = 40;
    clock_t startTime = clock();
    std::vector<bool> row;
    for(auto it = task.begin(); it != task.end(); ++it)
        if ((*it) == '^') row.push_back(1);
        else row.push_back(0);
//    std::vector<bool> temp(row.size(), 0);
//    std::cout << temp.size() << std::endl;
    
    static int counter = 0;
    for(int i = 0; i < iterations; ++i)
    {
        for(auto it = row.begin(); it != row.end(); ++it)
            if (!*it) ++counter;
        std::vector<bool> temp;
        temp.push_back(row[1]);
//        temp[0] = row[1];
        for(int j = 1; j < row.size() - 1; ++j)
            //temp[i] = row[j - 1] ^ row[j + 1];
            temp.push_back(row[j - 1] ^ row[j + 1]);
        temp.push_back(row[row.size() - 2]);
        //temp[row.size() - 1] = row[row.size() - 2];
        row = temp;
        //row.swap(temp);
//        std::cout << counter << std::endl;
    }
    float totalTime = float(clock() - startTime) / CLOCKS_PER_SEC;
    std::cout << counter << " safe tiles in " << iterations << " rows, " << totalTime << " seconds";
    std::cin.get();
    return 0;
}