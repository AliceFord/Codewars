function nbYear(p0, percent, aug, p) {
    let iterator = 1
    while (true) {
        p0 = p0 * (1 + percent / 100) + aug;
        if (p0 >= p) return iterator;
        iterator++;
    }
}


console.log(nbYear(1500, 5, 100, 5000));