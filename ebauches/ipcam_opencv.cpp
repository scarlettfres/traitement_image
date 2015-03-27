#include <iostream>
#include "opencv2/opencv.hpp"

using namespace std;
using namespace cv;

int main()
{
    VideoCapture cap("http://192.168.1.7:65534/videostream.cgi?user=admin&pwd=123456&resolution=32"); //change this URL according to your camera
    if (!cap.isOpened())
    {
        cout << "could not capture";
        return 0;
    }

    Mat frame;
    namedWindow("IPcamera", 1);
    char key = 'a';

    while(key != 27)
    {
        cap.grab();
        cap.retrieve(frame);
        imshow("IPcamera", frame);
        key = waitKey(10);
    }

    destroyAllWindows();
    return 0;
}

