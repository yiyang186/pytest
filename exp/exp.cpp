#include <iostream>
#include <cmath>
#include <set>
#include <iomanip>

#define ITER 30
#define K_NUM 10

using namespace std;

int K[K_NUM];

void init_K() {
  int j = 1;
  for(int i = 0; i < K_NUM; i++) {
    j = 3 * j + 1;
    K[i] = j;
  }
}


void single_iter(int i, double *x_cur, double *y_cur, double *angle_i) {
  double pow2_i = pow(2., -i);
  double angle_iter = atanh(pow2_i);
  double x_next, y_next, angle_next;

  if(*angle_i > 0) {
    x_next = *x_cur + *y_cur * pow2_i;
    y_next = *y_cur + *x_cur * pow2_i;
    angle_next = *angle_i - angle_iter;
  } else {
    x_next = *x_cur - *y_cur * pow2_i;
    y_next = *y_cur - *x_cur * pow2_i;
    angle_next = *angle_i + angle_iter;
  }

  *x_cur = x_next;
  *y_cur = y_next;
  *angle_i = angle_next;
}


double cr_exp(double x, int iter) {
  double log_2 = log(2.);
  int q = (int)(x / log_2);
  double input_value = fmod(x, log_2);

  double x_cur, y_cur, angle_i;
  double result;
  int index_K = 0;

  for(int i = 1; i < iter; i++) {
    if(i == 1) {
      // cout << i << endl;
      x_cur = 1.20749706;
      // cout << x_cur << endl;
      y_cur = 0.;
      angle_i = input_value;
    }

    if(i == K[index_K]) {
      // cout << "Ki " << i << endl;
      single_iter(i, &x_cur, &y_cur, &angle_i);
      index_K++;
    }
    single_iter(i, &x_cur, &y_cur, &angle_i);
    // cout << "angle_i " << angle_i << endl;
 
  }
  result = (x_cur + y_cur) * pow(2, q);
  return result;
}


int main() {
  int prec = 20;
  init_K();
  
  double x;
  int iter;
  cin >> iter >> x;

  double y0 = exp(x);
  cout << setprecision(prec) << fixed;
  cout << "real value is " << y0 << endl;

  double y1 = cr_exp(x, iter);
  cout << "calculate by codic " << y1 << endl;

  cout << setprecision(prec) << scientific;
  cout << "exp absolute error is " << abs(y1 - y0) << endl;
  cout << "exp relative error is " << abs(y1 - y0) / y0 << endl;

  return 0;
}
