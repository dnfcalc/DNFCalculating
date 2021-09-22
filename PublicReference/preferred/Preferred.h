#pragma once

#include <vector> 
using namespace std;
#define DLLEXPORT extern "C" __declspec(dllexport)

//计算择优范围
vector<int> range(double* array) {
    vector<int> range;
    for (int i = 0; i < 6; i++) {
        if (array[i] != 0) {
            range.push_back(i);
        }
    }
    if (range.size() == 0) {
        range.push_back(0);
    }
    return range;
}

//取最小值
int min(int num1, int num2)
{
    if (num1 < num2)
        return num1;
    else
        return num2;
}

//计算择优范围 buff
vector<int> range_buff(int sign) {
    vector<int> range;
    if (sign != 0) {
        for (int i = 1; i < 7; i++) {
            range.push_back(i);
        }
    }
    if (range.size() == 0) {
        range.push_back(0);
    }
    return range;
}
