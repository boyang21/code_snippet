#include <iostream>
#include <unistd.h>
int main(void) {
  pid_t kid;
  kid = fork();
  std::cout << "main here" << std::endl;
  if (kid == 0) {
    std::cout << "[CHILD]: here" << std::endl;
    return 0;
  }
  std::cout << "[OUT]: started child with pid=" << kid << std::endl;
  while(!std::cin.eof()) {
    std::string line;
    std::getline(std::cin, line);
    if (line.size() > 0)
      std::cout << "[OUT] " << line << std::endl;
  }
  std::cout << "[OUT ] end of file" << std::endl;
  return 0;

}
