# DrinkFinder

### Descrição

Um linguagem onde a entrada é uma cadeia de ingredientes e a saída é o drink que é possível fazer com eles ou o melhor match possível.

### ABNT 

program         = IngredientList

IngredientList  = "Com" Ingredient *("," Ingredient)  ; Ex: Com Cachaça, Lime, Sugar

Ingredient      = MainAlcohol / Fruit / Sweetener / Other / STRING

MainAlcohol     = "Cachaça" / "Vodka" / "Tequila" / "Rum" / "Gin"

Fruit           = "Lime" / "Lemon" / "Pineapple" / "Strawberry"

Sweetener       = "Sugar" / "Honey" / "Syrup"

Other           = "Mint" / "Soda" / "GingerBeer" / "Ice"

--- Tokens ---
STRING          = DQUOTE *CHAR DQUOTE  ; Para ingredientes customizados

### Coisas a aplicar

1) Banco de receitas (tipo um symboltable mas já montado)
2) Parser para analísar a entrada, checar com o banco de receitas e devolver a saída
3) tokenizer para garantir o que foi enviado

O legal é que não importa se eu envie ingrediente a mais ou a menos, ele me devolver o que tiver melhor match.