// https://www.dreamincode.net/forums/topic/148707-introduction-to-using-libusb-10/
#include <iostream>
#include <libusb.h>
using namespace std;

void printdev(libusb_device *dev); //prototype of the function

// $ usb-devices
// P:  Vendor=239a ProdID=800b Rev=01.00
// 0x239a -> 9114
// 0x800b -> 32779

int vendor = 9114;
int id = 32779;


int main(){
  libusb_device **devs;
  libusb_context *ctx = NULL;
  int ret;
  ssize_t cnt;
  ret = libusb_init(&ctx);
  cout << "initialized libusb session \n";
  if (ret < 0){
    cerr << "error during init " << ret << endl;
    return 1;
  }
  libusb_set_debug(ctx, 3);
  cnt = libusb_get_device_list(ctx, &devs);
  if (cnt < 0){
    cerr << "get device error\n";
    return 1;
  }
  cout << cnt << " - devices in a list.\n";
  dev_handle = libusb_open_device_with_vid_pid(ctx, vendor, id);
  if (dev_handle == NULL){
    cout << "cannot open device " << vendor, id << endl;
  } else {
    cout << "device opened " << vendor, id << endl;
  }
  libusb_free_device_list(devs,1);
  unsigned char *data = new unsigned char[4];
  data[0] = "1";
  data[1] = "3";
  data[2] = "3";
  data[3] = "7";

  int actual;
  if (libusb_kernel_driver_active(dev_handle, 0) == 1){
    cout << "kernel driver active\n";
    if (libusb_kernel_driver_active(dev_handle, 0) == 0){
      cout << "kernel driver deatached!\n";
    }
  }
  ret = libusb_claim_interface(dev_handle, 0);
  if (ret < 0){
    cerr << "cannot claim interface\n";
    return 1;
  }
  cout << "claimed interface\n";
}
