#include "person.pb.h"
#include <fstream>
#include <iostream>

using namespace std;
using namespace example;

int main() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;
  People pers;
  Person *p = pers.add_person();
  p->set_id(2);
  p->set_name("yypeng");
  p = pers.add_person();
  p->set_id(3);
  p->set_name("pengyy");

  ofstream outFile("person_cpp.bin", ios::out | ios::binary);
  pers.SerializeToOstream(&outFile);
  outFile.close();

  People pers1;
  ifstream inFile("person_cpp.bin",ios::in|ios::binary);
  pers1.ParseFromIstream(&inFile);
  inFile.close();

  for(int i = 0; i < pers1.person_size(); i++) {
    const Person &p = pers1.person(i);
    cout << p.id() << ", " << p.name() << endl;
  }

  People pers2;
  ifstream inFile2("person_py.bin",ios::in|ios::binary);
  pers2.ParseFromIstream(&inFile2);
  inFile2.close();

  for(int i = 0; i < pers2.person_size(); i++) {
    const Person &p = pers2.person(i);
    cout << p.id() << ", " << p.name() << endl;
  }
}
