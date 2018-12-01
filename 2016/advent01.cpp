#include<iostream>
#include<fstream>
#include<set>
#include<map>

int code(int x, int y)
{
	return (x < 0) * 100000000 + abs(x) * 100000 + (y < 0) * 1000 + abs(y);
}

int main()
{
	int direction = 0; // 0 - up, 1 - right, 2 - down, 3 - left
	int x = 0;
	int y = 0;

	std::ifstream finput("input1.txt");
	bool **coord = new bool*[1000];
	for (int i = 0; i < 1000; ++i)
	{
		coord[i] = new bool[1000];
		for (int j = 0; j < 1000; ++j)
			coord[i][j] = false;
	}
	int x_vis, y_vis;
	bool flag = false;

	while(!finput.eof())
	{
		char buf;
		finput >> buf;
		if (buf == ' ')
			finput >> buf;
		if (buf == 'R') direction = ++direction % 4;
		else if (buf == 'L') direction = (direction == 0)*3 + (direction != 0)* (--direction);
		finput >> buf;
		int val = 0;
		while (buf != ',' && !finput.eof())
		{
			val = val * 10 + (buf - '0');
			finput >> buf;
		}
		coord[x+500][y+500] = true;
		int dy = 0; int dx = 0;
		if (direction % 2 == 0) dy = (direction == 0) - (direction == 2);
		else dx = (direction == 1) - (direction == 3);
		for (; val > 0; --val) {
			x += dx;
			y += dy;
			if (!flag) {
				if (coord[x+500][y+500] == true) {
					x_vis = x; y_vis = y; flag = true;
				}
				else coord[x+500][y+500] = true;
			}
		}
	}

	std::cout << "x = " << x << " ,"
		<< "y = " << y << ", "
		<< "|x| + |y| = " << abs(x) + abs(y) << std::endl;
	std::cout << "I visited coordinates x = " << x_vis << ", y = " << y_vis << " twice!" << std::endl;
	std::cin.get();

	return 0;
}