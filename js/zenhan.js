function zenhan(day) {
    const zen = "０１２３４５６７８９／（）、～　";
    const han = "0123456789/(),~ ";
    const dic = Object.fromEntries([...zen].map((c, i) => [c, han[i]]));
    const res = [...day].map(c => dic[c] || c).join("");
    return res;
  }