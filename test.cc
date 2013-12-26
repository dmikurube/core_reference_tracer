#include <iostream>
#include <string>

#include <google/coredumper.h>


struct struct_a_t {
  int a[50];
  int x;
  std::string s;
};

struct struct_b_t {
  int x;
  struct_a_t d;
  struct_a_t* p;
};

int main() {
  struct_a_t a1, a2, a3;
  struct_b_t b;
  b.d = a1;
  b.p = &a2;

  struct_b_t* p = new struct_b_t();
  p->d = a3;
  p->p = &a2;

  WriteCoreDump("core.test");

  return 0;
}
