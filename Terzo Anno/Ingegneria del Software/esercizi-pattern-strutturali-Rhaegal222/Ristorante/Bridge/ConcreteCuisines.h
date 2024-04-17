#ifndef __CONCRETECUISINES__H__
#define __CONCRETECUISINES__H__

#include "CuisineType.h"
#include <string>

// Implementazione concreta per la cucina italiana.
class ItalianCuisine : public CuisineType {
public:
    std::string describeCuisine() override {
        return "La cucina italiana è famosa per la sua diversità regionale,\nl'enfasi su ingredienti freschi e di alta qualità, e la sua semplicità,\ncon molti piatti che hanno pochi ingredienti ma sono incredibilmente saporiti.\nPizze, pasta, risotti e formaggi sono tra i suoi piatti più noti.\n";
    }
};

// Implementazione concreta per la cucina giapponese.
class JapaneseCuisine : public CuisineType {
public:
    std::string describeCuisine() override {
        return "La cucina giapponese, conosciuta per la sua enfasi su ingredienti freschi e di stagione,\nè caratterizzata da piatti come sushi, sashimi, ramen e tempura. È apprezzata a livello globale\nper il suo equilibrio di gusto, presentazione minimalista e tecniche culinarie raffinate.\n";
    }
};

#endif  //!__CONCRETECUISINES__H__
