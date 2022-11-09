#include "org_gnoll_DiceNotationParser.h"
#include <unistd.h>
#include "shared_header.h"
#include <jni.h>

JNIEXPORT jint JNICALL Java_org_gnoll_DiceNotationParser_roll
  (JNIEnv* env, jclass jc, jstring  js)
{
    char* dieString = (char *)(*env)->GetStringUTFChars(env, js, JNI_FALSE);
    int return_code = roll_and_write(dieString, "output.dice");
    return return_code; //(*env)->NewIntArray(env, return_code);
}
