#include "Preferred.h"

//返回最大值索引 输出系
DLLEXPORT void cal_index(double data[9][6], int* index) {
    double max = 0;
    vector<int> list[8];
    for (int i = 0; i < 8; i++) {
        list[i] = range(data[i + 1]);
    }
    for (auto a1 = list[0].cbegin(); a1 != list[0].cend(); a1++)
    {
        for (auto a2 = list[1].cbegin(); a2 != list[1].cend(); a2++)
        {
            for (auto a3 = list[2].cbegin(); a3 != list[2].cend(); a3++)
            {
                for (auto a4 = list[3].cbegin(); a4 != list[3].cend(); a4++)
                {
                    for (auto a5 = list[4].cbegin(); a5 != list[4].cend(); a5++)
                    {
                        for (auto a6 = list[5].cbegin(); a6 != list[5].cend(); a6++)
                        {
                            for (auto a7 = list[6].cbegin(); a7 != list[6].cend(); a7++)
                            {
                                for (auto a8 = list[7].cbegin(); a8 != list[7].cend(); a8++)
                                {
                                    double k[6] = { data[0][0],data[0][1], data[0][2], data[0][3], data[0][4], data[0][5] };
                                    k[*a1] += data[1][*a1];
                                    k[*a2] += data[2][*a2];
                                    k[*a3] += data[3][*a3];
                                    k[*a4] += data[4][*a4];
                                    k[*a5] += data[5][*a5];
                                    k[*a6] += data[6][*a6];
                                    k[*a7] += data[7][*a7];
                                    k[*a8] += data[8][*a8];
                                    double sum = k[0] * k[1] * int(k[2]) * k[3] * k[4] * k[5];
                                    if (sum > max) 
                                    {
                                        max = sum;
                                        index[0] = *a1;
                                        index[1] = *a2;
                                        index[2] = *a3;
                                        index[3] = *a4;
                                        index[4] = *a5;
                                        index[5] = *a6;
                                        index[6] = *a7;
                                        index[7] = *a8;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

//辅助系
//0 奶妈 系数665
int buff_attack_0[41] = { 0, 38, 40, 42, 43, 44, 46, 48, 49, 51, 52, 53, 55, 57, 58, 60, 61, 62, 64, 66, 68, 69, 70, 72, 74, 75, 77, 78, 79, 81, 83, 84, 86, 87, 88, 90, 92, 93, 95, 96, 98 };
int buff_power_0[41] = {0, 148, 158, 169, 179, 189, 198, 208, 218, 228, 239, 249, 259, 269, 279, 290, 299, 309, 319, 329, 339, 349, 360, 370, 380, 390, 399, 409, 420, 430, 440, 450, 460, 470, 481, 491, 500, 510, 520, 530, 541};

//1 奶萝 系数665
int buff_attack_1[41] = { 0, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58, 60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 87 };
int buff_power_1[41] = { 0, 131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291, 300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478 };

//2 奶爸 系数620
int buff_attack_2[41] = { 0, 43, 44, 46, 48, 49, 51, 53, 54, 56, 58, 59, 61, 63, 64, 66, 68, 69, 71, 73, 75, 76, 78, 80, 81, 83, 85, 86, 88, 90, 91, 93, 95, 96, 98, 100, 101, 103, 105, 106, 109 };
int buff_power_2[41] = { 0, 164, 175, 186, 198, 209, 219, 230, 241, 253, 264, 275, 286, 298, 309, 320, 330, 341, 353, 364, 375, 386, 398, 409, 420, 431, 441, 453, 464, 475, 486, 498, 509, 520, 531, 543, 553, 564, 575, 586, 598 };

//系数750
int awake_power_0[41] = { 0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668 };


class Char
{
public:
    Char() {};
    ~Char() {};
    int type = 0;
    int preferred[6] = {};
    double burst_rate = 1.0;

    int buff_apply;
    int buff_lv;
    int buff_power_add;
    int buff_attack_add;
    double buff_rate;
    double buff_power_per;
    double buff_attack_per;
    
    int awake_apply;
    int awake_lv;
    int awake_power_add;
    double awake_rate;
    double awake_power_per;

    int other_power;
    int other_attack;
    int std_power;
    int std_attack;
    double sys_rate;
    double sys_base;
    double cal();

private:
    long buff_power = 0;
    long buff_attack = 0;
    long awake_power = 0;
    long resident_power = 0;
    long resident_attack = 0;
    long burst_power = 0;

    void cal_buff();
    void cal_awake();
    void cal_sum();
    double increase(long, long);
};

void Char::cal_buff(){
    double rate = 0.0;
    switch (type)
    {
    case 0:
        rate = buff_apply / 665.0 + 1;
        buff_power = (long)((buff_power_0[min(40, buff_lv)] + buff_power_add) * buff_power_per * buff_rate * rate);
        buff_attack = (long)((buff_attack_0[min(40, buff_lv)] + buff_attack_add) * buff_attack_per * buff_rate * rate);
        break;
    case 1:
        rate = buff_apply / 665.0 + 1;
        buff_power = (long)((buff_power_1[min(40, buff_lv)] + buff_power_add) * buff_power_per * buff_rate * rate);
        buff_attack = (long)((buff_attack_1[min(40, buff_lv)] + buff_attack_add) * buff_attack_per * buff_rate * rate);
        break;
    case 2:
        rate = buff_apply / 620.0 + 1;
        buff_power = (long)((buff_power_2[min(40, buff_lv)] + buff_power_add) * buff_power_per * buff_rate * rate);
        buff_attack = (long)((buff_attack_2[min(40, buff_lv)] + buff_attack_add) * buff_attack_per * buff_rate * rate);
        break;
    default:
        break;
    }

}

void Char::cal_awake() {
    awake_power = (long)((awake_power_0[min(40, awake_lv)] + awake_power_add) * awake_power_per * awake_rate * (awake_apply / 750.0 + 1));
}

void Char::cal_sum() {
    cal_buff();
    cal_awake();
    resident_power = buff_power + other_power;
    resident_attack = buff_attack + other_attack;
    burst_power = resident_power + awake_power;
}

double Char::increase(long power, long attack) {
    double x, y = 0;
    x = ((std_power + (std_power - 950.0) * sys_rate + sys_base) / 250.0 + 1) * std_attack;
    y = ((power + std_power + (std_power - 950.0) * sys_rate + sys_base) / 250.0 + 1) * (std_attack + attack);
    return y / x;
}

double Char::cal() {
    cal_sum();
    double resident = increase(resident_power, resident_attack);
    double burst = increase(burst_power, resident_attack);
    return resident * (1.0 - burst_rate) + burst * burst_rate;
}


//空属性
void attr_0(Char &c) {
}

//残香1
void attr_1(Char &c) {
    c.buff_power_per *= 1.03;
    c.awake_power_add += 60;
}
void attr_2(Char &c) {
    c.buff_power_per *= 1.04;
    c.awake_power_per *= 1.03;
}
void attr_3(Char &c) {
    c.buff_attack_per *= 1.04;
    c.awake_power_add += 25;
}
void attr_4(Char &c) {
    c.buff_attack_per *= 1.03;
    c.awake_power_per *= 1.03;
}
void attr_5(Char &c) {
    c.buff_apply += 185;
    c.awake_apply += 185;
}
void attr_6(Char &c) {
    c.awake_lv += 1;
    c.buff_power_per *= 1.03;
}
//残香2
void attr_7(Char &c) {
    c.buff_power_per *= 1.03;
    c.awake_power_add += 40;
}
void attr_8(Char &c) {
    c.buff_power_per *= 1.04;
    c.awake_power_per *= 1.02;
}
void attr_9(Char &c) {
    c.buff_attack_per *= 1.03;
    c.awake_power_add += 25;
}
void attr_10(Char &c) {
    c.buff_attack_per *= 1.02;
    c.awake_power_per *= 1.03;

}
void attr_11(Char &c) {
    c.buff_apply += 145;
    c.awake_apply += 145;
}
void attr_12(Char &c) {
    c.buff_lv += 1;
    c.awake_power_add += 30;
}
//武器
void attr_13(Char &c) {
    c.buff_power_per *= 1.03;
    c.awake_power_add += 60;
}
void attr_14(Char &c) {
    c.buff_power_per *= 1.05;
    c.awake_power_per *= 1.03;
}
void attr_15(Char &c) {
    c.buff_attack_per *= 1.04;
    c.awake_power_add += 40;
}
void attr_16(Char &c) {
    c.buff_attack_per *= 1.02;
    c.awake_power_per *= 1.05;
}
void attr_17(Char &c) {
    c.buff_apply += 180;
    c.awake_apply += 180;
}
void attr_18(Char &c) {
    c.buff_power_per *= 1.04;
    c.awake_lv += 1;
}
//戒指、辅助装备、下装
void attr_19(Char &c) {
    c.buff_power_per *= 1.04;
    c.awake_power_add += 40;
}
void attr_20(Char &c) {
    c.buff_power_per *= 1.05;
    c.awake_power_per *= 1.02;
}
void attr_21(Char &c) {
    c.buff_attack_per *= 1.04;
    c.awake_power_add += 25;
}
void attr_22(Char &c) {
    c.buff_attack_per *= 1.02;
    c.awake_power_per *= 1.04;
}
void attr_23(Char &c) {
    c.buff_apply += 160;
    c.awake_apply += 160;
}
void attr_24(Char &c) {
    c.buff_lv += 1;
    c.awake_power_add += 40;
}


void (*attr_list[4][7])(Char&) = { {attr_0,attr_1,attr_2,attr_3,attr_4,attr_5,attr_6},
     {attr_0,attr_7,attr_8,attr_9,attr_10,attr_11,attr_12},
     {attr_0,attr_13,attr_14,attr_15,attr_16,attr_17,attr_18},
     {attr_0,attr_19,attr_20,attr_21,attr_22,attr_23,attr_24}};

DLLEXPORT void cal_index_buff(int* range, int* i_data, double* d_data) {
    Char c;
    c.type = i_data[0];
    c.buff_apply = i_data[1];
    c.buff_lv = i_data[2];
    c.buff_power_add = i_data[3];
    c.buff_attack_add = i_data[4];
    c.awake_apply = i_data[5];
    c.awake_lv = i_data[6];
    c.awake_power_add = i_data[7];
    c.other_power = i_data[8];
    c.other_attack = i_data[9];
    c.std_power = i_data[10];
    c.std_attack = i_data[11];
    c.burst_rate = d_data[0];
    c.buff_rate = d_data[1];
    c.buff_power_per = d_data[2];
    c.buff_attack_per = d_data[3];
    c.awake_rate = d_data[4];
    c.awake_power_per = d_data[5];
    c.sys_rate = d_data[6];
    c.sys_base = d_data[7];

    vector<int> list[6];
    for (int i = 0; i < 6; i++) {
        list[i] = range_buff(range[i]);
    }
    double max = 0;
    if (list[3][0] * list[4][0] * list[5][0] != 0) 
    {
        for (auto a1 = list[0].cbegin(); a1 != list[0].cend(); a1++)
        {
            for (auto a2 = list[1].cbegin(); a2 != list[1].cend(); a2++)
            {
                for (auto a3 = list[2].cbegin(); a3 != list[2].cend(); a3++)
                {
                    for (auto a4 = list[3].cbegin(); a4 != list[3].cend(); a4++)
                    {
                        for (auto a5 = list[4].cbegin(); a5 != list[4].cend(); a5++)
                        {
                            for (auto a6 = list[5].cbegin(); a6 != list[5].cend(); a6++)
                            {
                                if ((*a4 >= *a5) & (*a5 >= *a6)) {
                                    Char p = c;
                                    attr_list[0][*a1](p);
                                    attr_list[1][*a2](p);
                                    attr_list[2][*a3](p);
                                    attr_list[3][*a4](p);
                                    attr_list[3][*a5](p);
                                    attr_list[3][*a6](p);
                                    double result = p.cal();
                                    if (result > max) {
                                        max = result;
                                        range[0] = *a1;
                                        range[1] = *a2;
                                        range[2] = *a3;
                                        range[3] = *a4;
                                        range[4] = *a5;
                                        range[5] = *a6;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    else {
        for (auto a1 = list[0].cbegin(); a1 != list[0].cend(); a1++)
        {
            for (auto a2 = list[1].cbegin(); a2 != list[1].cend(); a2++)
            {
                for (auto a3 = list[2].cbegin(); a3 != list[2].cend(); a3++)
                {
                    for (auto a4 = list[3].cbegin(); a4 != list[3].cend(); a4++)
                    {
                        for (auto a5 = list[4].cbegin(); a5 != list[4].cend(); a5++)
                        {
                            for (auto a6 = list[5].cbegin(); a6 != list[5].cend(); a6++)
                            {
                                Char p = c;
                                attr_list[0][*a1](p);
                                attr_list[1][*a2](p);
                                attr_list[2][*a3](p);
                                attr_list[3][*a4](p);
                                attr_list[3][*a5](p);
                                attr_list[3][*a6](p);
                                double result = p.cal();
                                if (result > max) {
                                    max = result;
                                    range[0] = *a1;
                                    range[1] = *a2;
                                    range[2] = *a3;
                                    range[3] = *a4;
                                    range[4] = *a5;
                                    range[5] = *a6;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}