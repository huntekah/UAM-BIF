// Program designed to crack md5
#include <iostream>
#include <string>
#include "md5.h"
#include <sstream>
#include <iomanip>
 
using std::cout; using std::endl;

int similarity = 10;

std::string hex_to_ascii(std::string hex){
    //in: "48656c6c6f"; (48 65 6c 6c 6f)
    //out: "Hello";
    int len = hex.length();
    std::string newString;
    for(int i=0; i< len; i+=2)
    {
        std::string byte = hex.substr(i,2);
        char chr = (char) (int)strtol(byte.c_str(), NULL, 16);
        newString.push_back(chr);
    }
    return newString;
}

std::string ascii_to_hex(const std::string& ascii){
    std::ostringstream ret;

    unsigned int c;
    for(std::string::size_type i = 0; i<ascii.length();i++){
        c = (unsigned int)(unsigned char)ascii[i];
        ret << std::hex << std::setfill('0') <<  std::setw(2) << std::nouppercase << c;
    }
    return ret.str();
}

std::string custom_md5(std::string ciphertext, std::string indeks){
    //std::string index_hex = hex_to_ascii(indeks);
    std::string out = md5(hex_to_ascii(md5(indeks + ciphertext))).substr(0,similarity-3);
    return out;
}

std::string custom_md5_hare(std::string ciphertext, std::string indeks){
    //std::string index_hex = hex_to_ascii(indeks);
    std::string partial = custom_md5(ciphertext,indeks);
    std::string out = custom_md5(partial,indeks);
    return out;
}

std::string custom_md5_full(std::string ciphertext, std::string indeks){
    //std::string index_hex = hex_to_ascii(indeks);
    std::string out = md5(hex_to_ascii(md5(indeks + ciphertext)));
    return out;
}


bool are_almost_equal(std::string hare, std::string tortoise){
    // cout << hare.substr(0,18) << tortoise.substr(0,18) <<endl; 
    // return hare.substr(0,18) == tortoise.substr(0,18);
    //cout << hare.substr(0,6) << tortoise.substr(0,6) <<endl; 
    return hare.substr(0,similarity) == tortoise.substr(0,similarity-3);
}

void Floyd(std::string indeks){
    /**tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1
    **/
   std::string starting_token = "YOLO";
   std::string indeks_hex = hex_to_ascii(indeks);
   std::string hare = custom_md5_hare(starting_token,indeks_hex);
   std::string tortoise = custom_md5(starting_token,indeks_hex);
    int cnt = 0;
    int Mhash = 0;
   while (!are_almost_equal(hare, tortoise))
   {
       cnt+=1;
       if (cnt % 1000000 == 0) {
           Mhash+=1;
           cnt = 0;
           cout << Mhash << "Mhash .operations\n";
           cout << "hare is " << hare << endl;
           cout << "while tortoise is " << tortoise << endl;
       }
        tortoise = custom_md5(tortoise,indeks_hex);
        hare = custom_md5_hare(hare, indeks_hex);
   }
   int mu = 0;
   //tortoise = custom_md5(starting_token,indeks_hex);
   //hare = tortoise;
   tortoise = starting_token;

    cout<< "Wow, I found a cycle, looking for the collision now sir!" <<endl;
    cout<< Mhash << "." << cnt << "Mhash Operations" << endl;

   std::string colliding_hare = "";
   std::string colliding_tortoise = "";
   while (!are_almost_equal(hare, tortoise))
   {
        cnt+=1;
       if (cnt % 1000000 == 0) {
           Mhash+=1;
           cnt = 0;
           //cout << Mhash << "Mhash ..operations\n";
       }
        colliding_hare = hare;
        colliding_tortoise = tortoise;
        tortoise = custom_md5(tortoise,indeks_hex);
        hare = custom_md5(hare, indeks_hex);
   }

    cout<< Mhash << "." << cnt << "Mhash Operations later..." << endl;
    cout << "Collision is:\n" << "\t" + indeks + " " + ascii_to_hex(colliding_hare) + "\n\t" + indeks + " " + ascii_to_hex(colliding_tortoise) + "\n";
    cout << "See for yourself!\n"<< "\t" + hare + "\n\t" + tortoise + "\n";
    cout << "full version:\n"<< "\t" + custom_md5_full(colliding_hare,indeks_hex) \
         + "\n\t" + custom_md5_full(colliding_tortoise,indeks_hex) + "\n";

}

int main(int argc, char *argv[])
{
    cout << "md5 of 'grape': " << md5("grape") << endl;
    //cout << md5(hex_to_ascii(md5("renmich1123376350383621786626"))) << endl;
    //cout << md5(hex_to_ascii(md5("renmich3700873222361195459231"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "dc4eb2a3d9c197e7be878ac7bc2a1a4f"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "65b08336e344eed02bba15d3b68d0d49"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "77a725d103118b5763c3ba3c1a6927ee"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "ee59997df0c00889e251e19d1067be94"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "400c992"))) << endl;
    cout << md5(hex_to_ascii(md5(hex_to_ascii("452088") +  "0b30b96"))) << endl;
    cout<<endl;
    //452262 65646264653862
    //    452262 65653230666561
    cout << md5(hex_to_ascii(md5( hex_to_ascii("45226265646264653862") ))) << endl;
    cout << md5(hex_to_ascii(md5( hex_to_ascii("45226265653230666561") ))) << endl;
        
    //bool ok = are_almost_equal(md5(hex_to_ascii(md5("renmich0123376350383621786626"))),md5(hex_to_ascii(md5("renmich3700873222361195459231"))));
    //cout << ok <<endl;
    Floyd("452088");
    // for(int i=452000;i<452999;i++){
    //     Floyd(std::to_string(i));
    // }
    return 0;
}
