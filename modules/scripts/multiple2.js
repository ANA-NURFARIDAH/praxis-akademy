const company = "Pesantren Ahli IT";

function sum(firts, second) {
    return firts + second;
}

class Company {

}

// export {company as perusahaan, sum as jumlah, Company as kerjaan}  //ini penggunaan export yang lebih enak, agar lebih mudah dan fokus
export {company, sum, Company} //ini manggil dengan cara yang asi tanpa alias