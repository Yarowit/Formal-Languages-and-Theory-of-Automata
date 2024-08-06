for f in $(ls Kompilator/Przykłady)
do
    echo $f
    python3 Kompilator.py Kompilator/Przykłady/$f lop
    ./maszyna-wirtualna-cln lop
done

for f in $(ls Kompilator/Maszyna)
do
    echo $f
    python3 Kompilator.py Kompilator/Maszyna/$f lop
    ./maszyna-wirtualna-cln lop
done