#include <stdio.h>
#include <string.h>
#include <unistd.h>

unsigned char arr[54];

#include <stdio.h>

int hmmm() {
    char msg[] = "Well, you figured something out, now enter your true XOR key in hex (e.g., 0xaa): ";
    unsigned char result[sizeof(arr)];
    unsigned int user_input_hex;
    unsigned char usr_inp;
    unsigned char arr[] = {
        0x8D, 0x90, 0x9A, 0x80, 0x95, 0xCF, 0x88, 0x96, 0xA4, 0xCA, 0x88, 0xA4, 0x8F, 0xCB, 0xCB, 0xA4, 0xC8, 0xCF, 0x81, 0x82, 0xA4, 0x9D, 0xCB, 0x89, 0xA4, 0x88, 0x8E, 0x98, 0x93, 0xA4, 0xCF, 0x95, 0xA4, 0xC8, 0x83, 0x8B, 0xC8, 0x89, 0xCA, 0xC8, 0x95, 0x98, 0xC8, 0x9F, 0xA4, 0x89, 0xC8, 0x8D, 0xC8, 0x89, 0x88, 0xC8, 0x89, 0x86
    };


    __asm__ __volatile__ (
        ".intel_syntax noprefix;"
        "mov rax, 1;"
        "mov rdi, 1;"
        "mov rsi, %0;"
        "mov rdx, %1;"
        "syscall;"
        ".att_syntax;"
        :
        : "r" (msg), "r" (sizeof(msg) - 1)
        : "rax", "rdi", "rsi", "rdx", "memory"
    );
    scanf("%x", &user_input_hex);
    usr_inp = (unsigned char)(user_input_hex & 0xFF);
    for (size_t i = 0; i < sizeof(arr); ++i) {
        __asm__ __volatile__ (
            ".intel_syntax noprefix;"
            "mov al, %2;"
            "mov bl, byte ptr [%1 + %0];"
            "xor bl, al;"
            "mov byte ptr [%3 + %0], bl;"
            ".att_syntax;"
            :
            : "r"(i), "r"(arr), "r"(usr_inp), "r"(result)
            : "al", "bl", "memory"
        );
    }
    __asm__ __volatile__ (
        ".intel_syntax noprefix;"
        "mov rax, 1;"
        "mov rdi, 1;"
        "mov rsi, %0;"
        "mov rdx, %1;"
        "syscall;"
        ".att_syntax;"
        :
        : "r"(result), "r"(sizeof(arr))
        : "rax", "rdi", "rsi", "rdx", "memory"
    );
    return 0;
}


int main() {
    char input[8];
    printf("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n");
    printf("⣿⣿⣿⣿⣿⣿⣿⠛⢩⣴⣶⣶⣶⣌⠙⠫⠛⢋⣭⣤⣤⣤⣤⡙⣿⣿⣿⣿⣿⣿\n");
    printf("⣿⣿⣿⣿⣿⡟⢡⣾⣿⠿⣛⣛⣛⣛⣛⡳⠆⢻⣿⣿⣿⠿⠿⠷⡌⠻⣿⣿⣿⣿\n");
    printf("⣿⣿⣿⣿⠏⣰⣿⣿⣴⣿⣿⣿⡿⠟⠛⠛⠒⠄⢶⣶⣶⣾⡿⠶⠒⠲⠌⢻⣿⣿\n");
    printf("⣿⣿⠏⣡⢨⣝⡻⠿⣿⢛⣩⡵⠞⡫⠭⠭⣭⠭⠤⠈⠭⠒⣒⠩⠭⠭⣍⠒⠈⠛\n");
    printf("⡿⢁⣾⣿⣸⣿⣿⣷⣬⡉⠁⠄⠁⠄⠄⠄⠄⠄⠄⠄⣶⠄⠄⠄⠄⠄⠄⠄⠄⢀\n");
    printf("⢡⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣿⣦⣤⣀⣀⣀⣀⠄⣤⣾\n");
    printf("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⡶⢇⣰⣿⣿⣟⠿⠿⠿⠿⠿⠿⠟⠁⣾\n");
    printf("⣿⣿⣿⣿⣿⣿⣿⡟⢛⡛⠿⠿⣿⣧⣶⣶⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣧⠸⣿⣿\n");
    printf("⠘⢿⣿⣿⣿⣿⣿⡇⢿⡿⠿⠦⣤⣈⣙⡛⠿⠿⠿⣿⣿⣿⣿⠿⠿⠟⠛⡀⢻⣿\n");
    printf("⠄⠄⠉⠻⢿⣿⣿⣷⣬⣙⠳⠶⢶⣤⣍⣙⡛⠓⠒⠶⠶⠶⠶⠖⢒⣛⣛⠁⣾⣿\n");
    printf("⠄⠄⠄⠄⠄⠈⠛⠛⠿⠿⣿⣷⣤⣤⣈⣉⣛⣛⣛⡛⠛⠛⠿⠿⠿⠟⢋⣼⣿⣿\n");
    printf("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⣻⣿⣿⣿⣿⡿⠿⠛⠃⠄⠙⠛⠿⢿\n");
    printf("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢬⣭⣭⡶⠖⣢⣦⣀⠄⠄⠄⠄⢀⣤⣾\n");
    printf("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣶⣶⣶⣾⣿⣿⣿⣿⣷⡄⠄⢠⣾⣿⣿\n");
    printf("Hey, i have something for you, but i can only give it to you XORed\n");
    printf("So quickly give me the XOR key as ASCII symbol:\n");
    fgets(input, sizeof(input), stdin);
    printf("Trying to use your XOR key...\n");
    sleep(5);
    printf("Well, that's disappointing, nothing happened ¯\\_(ツ)_/¯\n");
    printf("Maybe something isn't working fine\n");
    return 0;
}
