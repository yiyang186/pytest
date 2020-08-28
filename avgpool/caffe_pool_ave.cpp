#include<cstdio>
#include<cmath>
#include<algorithm>

enum ROUND_MODE {
  CEIL,
  FLOOR
};

void pooled_shape(int *pooled_height_,
                  int *pooled_width_,
                  int height_,
                  int width_,
                  int stride_h_,
                  int stride_w_,
                  int kernel_h_,
                  int kernel_w_,
                  int pad_h_,
                  int pad_w_,
  ROUND_MODE round_mode_) {
  switch (round_mode_) {
    case CEIL:
      *pooled_height_ = static_cast<int>(ceil(static_cast<float>(
          height_ + 2 * pad_h_ - kernel_h_) / stride_h_)) + 1;
      *pooled_width_ = static_cast<int>(ceil(static_cast<float>(
          width_ + 2 * pad_w_ - kernel_w_) / stride_w_)) + 1;
      break;
    case FLOOR:
      *pooled_height_ = static_cast<int>(floor(static_cast<float>(
          height_ + 2 * pad_h_ - kernel_h_) / stride_h_)) + 1;
      *pooled_width_ = static_cast<int>(floor(static_cast<float>(
          width_ + 2 * pad_w_ - kernel_w_) / stride_w_)) + 1;
      break;
    default:
      printf("Unknown rounding mode.\n");
  }
}

using namespace std;
void poolmethod_ave(float *top_data,
                    float *bottom_data,
                    int height_,
                    int width_,
                    int pooled_height_,
                    int pooled_width_,
                    int stride_h_,
                    int stride_w_,
                    int kernel_h_,
                    int kernel_w_,
                    int pad_h_,
                    int pad_w_) {
  for (int ph = 0; ph < pooled_height_; ++ph) {
    for (int pw = 0; pw < pooled_width_; ++pw) {
      int hstart = ph * stride_h_ - pad_h_;
      int wstart = pw * stride_w_ - pad_w_;
      int hend = min(hstart + kernel_h_, height_ + pad_h_);
      int wend = min(wstart + kernel_w_, width_ + pad_w_);
      int pool_size = (hend - hstart) * (wend - wstart);

      if ((ph == 0 || ph == pooled_height_ - 1) && (pw == 0 || pw == pooled_width_ - 1)) {
        printf("pool_size: %d = (%d - %d) * (%d - %d)\n",
             pool_size, hend, hstart, wend, wstart);
      }

      hstart = max(hstart, 0);
      wstart = max(wstart, 0);
      hend = min(hend, height_);
      wend = min(wend, width_);
      int count = 0;
      for (int h = hstart; h < hend; ++h) {
        for (int w = wstart; w < wend; ++w) {
          top_data[ph * pooled_width_ + pw] +=
              bottom_data[h * width_ + w];
	        ++count;
        }
      }

      if ((ph == 0 || ph == pooled_height_ - 1) && (pw == 0 || pw == pooled_width_ - 1)) {
        printf("     used: %d = (%d - %d) * (%d - %d)\n",
             count, hend, hstart, wend, wstart);
      }

      top_data[ph * pooled_width_ + pw] /= pool_size;
    }
  }
}

int main() {
  int height = 17;
  int width = 17;
  int stride_h = 1;
  int stride_w = 6;
  int kernel_h = 5;
  int kernel_w = 6;
  int pad_h = 1;
  int pad_w =1;
  ROUND_MODE mode = CEIL;

  int pooled_height = 0;
  int pooled_width = 0;
  pooled_shape(&pooled_height, &pooled_width,
	       height, width,
	       stride_h, stride_w,
	       kernel_h, kernel_w,
	       pad_h, pad_w,
	       mode);

  float *top_data = new float[pooled_height * pooled_width];
  float *bottom_data = new float[height * width];

  for (int i = 0; i < pooled_height * pooled_width; ++i)
    top_data[i] = 0;

  for (int i = 0; i < height * width; ++i)
    bottom_data[i] = i + 1;

  poolmethod_ave(top_data, bottom_data,
                 height, width,
                 pooled_height, pooled_width,
                 stride_h, stride_w,
                 kernel_h, kernel_w,
                 pad_h, pad_w);

  for (int i = 0; i < height; ++i) {
    for (int j = 0; j < width; ++j) {
      printf("\t%2d", (int)bottom_data[i * height + j]);
    }
    printf("\n");
  }

  for (int i = 0; i < pooled_height; ++i) {
    for (int j = 0; j < pooled_width; ++j) {
      printf("\t%5.2f", top_data[i * pooled_height + j]);
    }
    printf("\n");
  }

  delete []top_data;
  delete []bottom_data;
  
  return 0;
}
