#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdio.h>
#include <unistd.h>

using namespace cv;
using namespace std;

int ct = 0;
char tipka;
char filename[100]; // For filename
int c = 1;	    // For filename

int main(int, char **)
{
	Mat frame;
	VideoCapture cap;
	cap.open(0);
	int deviceID = 0;	 // 0 = open default camera
	int apiID = cv::CAP_ANY; // 0 = autodetect default API
				 // open selected camera using selected API
	cap.open(deviceID + apiID);
	if (!cap.isOpened())
	{
		cerr << "ERROR! Unable to open camera\n";
		return -1;
	}
	for (;;)
	{
		cap.read(frame);
		usleep(5);		   // Sleep is mandatory - for no leg!
		imshow("CAMERA 1", frame); // Window name
		tipka = cv::waitKey(30);
		if (tipka == 'q')
		{
			sprintf(filename, "Frame_%d.jpg", c); // select your folder - filename is "Frame_n"
			cv::waitKey(10);
			imshow("CAMERA 1", frame);
			imwrite(filename, frame);
			cout << "Frame_" << c << endl;
			c++;
		}
		if (tipka == 'a')
		{
			cout << "Terminating..." << endl;
			usleep(2000);
			break;
		}
	}
	return 0;
}
