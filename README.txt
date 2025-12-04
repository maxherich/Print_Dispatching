Print_Dispatching

Dispečink Tiskové Fronty  


Přehled

Tento skript demonstruje implementaci dispečera tiskáren pomocí vícevláknového programování v Pythonu. Cílem je zpracovávat požadavky na tisk (reprezentované třídou `Requirement`) zpracovávány omezeným počtem tiskáren (`Printer`).

Využívá se zde knihovna `threading` pro paralelní zpracování úloh.


Použité Mechanizmy

1.  Requirement: Představuje soubor nebo tiskovou úlohu, která má být vytištěna. Metoda execute() posílá požadavek do tiskárny.
2.  Printer: Reprezentuje tiskárnu.
    Využívá threading.Lock k zajištění, že v danou chvíli může tiskárna zpracovávat pouze jeden požadavek.
3.  PrintDispatcher: Spravuje skupinu tiskáren.
    Využívá threading.Semaphore k omezení počtu požadavků, které mohou být současně aktivně zpracovávány (na počet dostupných tiskáren).
    Metoda send_to_print čeká na volnou tiskárnu a poté jí přidělí požadavek.


Jak Spustit

Spusťte skript a zadávejte cestu souboru který chcete vytisknout.