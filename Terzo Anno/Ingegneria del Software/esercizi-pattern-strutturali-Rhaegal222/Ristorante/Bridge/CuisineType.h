#ifndef __CUISINETYPE__H__
#define __CUISINETYPE__H__

#include <string>

using namespace std;

// Astrazione per i tipi di cucina.
class CuisineType {
public:
    virtual ~CuisineType() = default;
    virtual string describeCuisine() = 0;
};

#endif  //!__CUISINETYPE__H__
