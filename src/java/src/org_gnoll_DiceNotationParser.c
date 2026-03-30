#include "org_gnoll_DiceNotationParser.h"
#include <unistd.h>
#include "shared_header.h"
#include <jni.h>

JNIEXPORT jint JNICALL Java_org_gnoll_DiceNotationParser_roll
  (JNIEnv* env, jclass jc, jstring js, jstring fn)
{
    char* dieString = (char *)(*env)->GetStringUTFChars(env, js, JNI_FALSE);
    char* fileName = (char *)(*env)->GetStringUTFChars(env, fn, JNI_FALSE);
    int return_code = roll_and_write(dieString, fileName);
    (*env)->ReleaseStringUTFChars(env, js, dieString);
    (*env)->ReleaseStringUTFChars(env, fn, fileName);
    return return_code;
}

JNIEXPORT jint JNICALL Java_org_gnoll_DiceNotationParser_validateRollRequest
  (JNIEnv* env, jclass jc, jstring js)
{
    char* dieString = (char *)(*env)->GetStringUTFChars(env, js, JNI_FALSE);
    int return_code = gnoll_validate_roll_request(dieString);
    (*env)->ReleaseStringUTFChars(env, js, dieString);
    return return_code;
}
