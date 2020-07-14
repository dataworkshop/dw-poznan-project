#pragma once
namespace Eloquent {
    namespace ML {
        namespace Port {
            class SVM {
                public:
                    SVM() {
                    }

                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        float kernels[41] = { 0 };
                        float decisions[10] = { 0 };
                        int votes[5] = { 0 };
                        kernels[0] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 12.0  , 0.0  , 0.0 );
                        kernels[1] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 68.0  , 0.0  , 0.0 );
                        kernels[2] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 84.0  , 0.0  , 0.0 );
                        kernels[3] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 76.0  , 0.0  , 0.0 );
                        kernels[4] = compute_kernel(x,   1.0  , 1.0  , 0.0  , 80.0  , 0.0  , 0.0 );
                        kernels[5] = compute_kernel(x,   0.0  , 0.0  , 0.0  , 91.0  , 0.0  , 0.0 );
                        kernels[6] = compute_kernel(x,   0.0  , 0.0  , 1.0  , 19.0  , 0.0  , 0.0 );
                        kernels[7] = compute_kernel(x,   0.0  , 0.0  , 1.0  , 22.0  , 0.0  , 0.0 );
                        kernels[8] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 86.0  , 0.0  , 0.0 );
                        kernels[9] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 78.0  , 0.0  , 0.0 );
                        kernels[10] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 77.0  , 0.0  , 0.0 );
                        kernels[11] = compute_kernel(x,   0.0  , 1.0  , 0.0  , 86.0  , 0.0  , 0.0 );
                        kernels[12] = compute_kernel(x,   1.0  , 1.0  , 0.0  , 77.0  , 0.0  , 0.0 );
                        kernels[13] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 78.0  , 0.0  , 0.0 );
                        kernels[14] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 77.0  , 0.0  , 0.0 );
                        kernels[15] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 12.0  , 0.0  , 0.0 );
                        kernels[16] = compute_kernel(x,   0.0  , 1.0  , 0.0  , 86.0  , 0.0  , 0.0 );
                        kernels[17] = compute_kernel(x,   1.0  , 0.0  , 0.0  , 91.0  , 0.0  , 0.0 );
                        kernels[18] = compute_kernel(x,   1.0  , 1.0  , 0.0  , 84.0  , 0.0  , 0.0 );
                        kernels[19] = compute_kernel(x,   0.0  , 0.0  , 0.0  , 86.0  , 0.0  , 0.0 );
                        kernels[20] = compute_kernel(x,   1.0  , 0.0  , 0.0  , 92.0  , 0.0  , 0.0 );
                        kernels[21] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 77.0  , 0.0  , 0.0 );
                        kernels[22] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 84.0  , 0.0  , 0.0 );
                        kernels[23] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 69.0  , 0.0  , 0.0 );
                        kernels[24] = compute_kernel(x,   1.0  , 0.0  , 0.0  , 22.0  , 0.0  , 0.0 );
                        kernels[25] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 78.0  , 0.0  , 0.0 );
                        kernels[26] = compute_kernel(x,   0.0  , 1.0  , 0.0  , 86.0  , 0.0  , 0.0 );
                        kernels[27] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 80.0  , 108.0  , 127.0 );
                        kernels[28] = compute_kernel(x,   1.0  , 0.0  , 1.0  , 86.0  , 0.0  , 0.0 );
                        kernels[29] = compute_kernel(x,   0.0  , 0.0  , 0.0  , 19.0  , 0.0  , 0.0 );
                        kernels[30] = compute_kernel(x,   1.0  , 0.0  , 1.0  , 86.0  , 0.0  , 0.0 );
                        kernels[31] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 80.0  , 0.0  , 0.0 );
                        kernels[32] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 13.0  , 0.0  , 0.0 );
                        kernels[33] = compute_kernel(x,   1.0  , 0.0  , 0.0  , 90.0  , 0.0  , 0.0 );
                        kernels[34] = compute_kernel(x,   0.0  , 0.0  , 1.0  , 24.0  , 0.0  , 0.0 );
                        kernels[35] = compute_kernel(x,   1.0  , 0.0  , 1.0  , 86.0  , 0.0  , 0.0 );
                        kernels[36] = compute_kernel(x,   1.0  , 1.0  , 0.0  , 35.0  , 0.0  , 0.0 );
                        kernels[37] = compute_kernel(x,   1.0  , 0.0  , 0.0  , 89.0  , 0.0  , 0.0 );
                        kernels[38] = compute_kernel(x,   1.0  , 1.0  , 1.0  , 79.0  , 0.0  , 0.0 );
                        kernels[39] = compute_kernel(x,   1.0  , 0.0  , 1.0  , 15.0  , 0.0  , 0.0 );
                        kernels[40] = compute_kernel(x,   1.0  , 0.0  , 1.0  , 86.0  , 0.0  , 0.0 );
                        decisions[0] = 18.0
                        + kernels[1] * 0.03125
                        + kernels[3] * -0.03125
                        ;
                        decisions[1] = -0.487133775926
                        + kernels[0] * 0.577320479507
                        + kernels[1]
                        + kernels[6] * -0.905890872485
                        + kernels[8] * -0.671429607022
                        ;
                        decisions[2] = -0.980099502488
                        + kernels[0]
                        + kernels[1]
                        - kernels[15]
                        + kernels[23] * -0.978742650384
                        + kernels[24] * -0.021257349616
                        ;
                        decisions[3] = -1.058130771015
                        + kernels[0]
                        + kernels[1]
                        - kernels[32]
                        + kernels[36] * -0.088187097177
                        + kernels[38] * -0.784972499028
                        + kernels[39] * -0.126840403795
                        ;
                        decisions[4] = -0.999629163579
                        + kernels[2]
                        + kernels[3] * 0.199998154801
                        + kernels[4] * 0.799520417884
                        + kernels[5] * -0.799595413183
                        + kernels[7] * -0.199923159502
                        - kernels[8]
                        ;
                        decisions[5] = -1.000000000001
                        + kernels[2]
                        + kernels[3]
                        + kernels[4]
                        + kernels[12] * -0.799999999999
                        + kernels[18] * -0.2
                        + kernels[21] * -0.200000000001
                        + kernels[22] * -0.986666666667
                        + kernels[23] * -0.013333333333
                        + kernels[25] * -0.8
                        ;
                        decisions[6] = -2.367944744
                        + kernels[2]
                        + kernels[3]
                        + kernels[4]
                        + kernels[27] * -2.4612434e-05
                        - kernels[31]
                        + kernels[33] * -0.836067154979
                        + kernels[36] * -0.163908232587
                        - kernels[38]
                        ;
                        decisions[7] = 0.000738218669
                        + kernels[5]
                        + kernels[6] * 0.499464992504
                        + kernels[7]
                        + kernels[8]
                        + kernels[11] * -0.361038968473
                        + kernels[15] * -0.612766027057
                        + kernels[16] * -0.13523628017
                        - kernels[19]
                        + kernels[23] * -0.8873443214
                        + kernels[24] * -0.500540586161
                        + kernels[26] * -0.002538809243
                        ;
                        decisions[8] = -1.298136477245
                        + kernels[5]
                        + kernels[6]
                        + kernels[7]
                        + kernels[8]
                        + kernels[29] * -0.884986177332
                        + kernels[31] * -0.904857390688
                        + kernels[33] * -0.176878451337
                        - kernels[34]
                        + kernels[35] * -0.033277980643
                        - kernels[40]
                        ;
                        decisions[9] = -1.147873496408
                        + kernels[9]
                        + kernels[10]
                        + kernels[13] * 4.3098e-07
                        + kernels[14]
                        + kernels[15]
                        + kernels[17]
                        + kernels[19]
                        + kernels[20]
                        + kernels[21]
                        + kernels[23]
                        + kernels[24]
                        + kernels[25] * 0.061483440203
                        + kernels[27] * -7.2486111e-05
                        + kernels[28] * -0.878294629147
                        + kernels[29] * -0.738794525838
                        + kernels[30] * -0.921961126818
                        - kernels[31]
                        - kernels[32]
                        - kernels[33]
                        + kernels[35] * -0.522361103268
                        - kernels[36]
                        - kernels[37]
                        - kernels[38]
                        - kernels[40]
                        ;
                        votes[decisions[0] > 0 ? 0 : 1] += 1;
                        votes[decisions[1] > 0 ? 0 : 2] += 1;
                        votes[decisions[2] > 0 ? 0 : 3] += 1;
                        votes[decisions[3] > 0 ? 0 : 4] += 1;
                        votes[decisions[4] > 0 ? 1 : 2] += 1;
                        votes[decisions[5] > 0 ? 1 : 3] += 1;
                        votes[decisions[6] > 0 ? 1 : 4] += 1;
                        votes[decisions[7] > 0 ? 2 : 3] += 1;
                        votes[decisions[8] > 0 ? 2 : 4] += 1;
                        votes[decisions[9] > 0 ? 3 : 4] += 1;
                        int val = votes[0];
                        int idx = 0;

                        for (int i = 1; i < 5; i++) {
                            if (votes[i] > val) {
                                val = votes[i];
                                idx = i;
                            }
                        }

                        return idx;
                    }

                protected:
                    /**
                    * Compute kernel between feature vector and support vector.
                    * Kernel type: linear
                    */
                    float compute_kernel(float *x, ...) {
                        va_list w;
                        va_start(w, 6);
                        float kernel = 0.0;

                        for (uint16_t i = 0; i < 6; i++) {
                            kernel += x[i] * va_arg(w, double);
                        }

                        return kernel;
                    }
                };
            }
        }
    }

unsigned char svm_action_classes[] = {'*', 'D', 'L', 'R', 'U'};
using namespace Eloquent::ML::Port;
SVM svm = SVM();

unsigned char svm_predict(float *x) {
    return svm_action_classes[svm.predict(x)];
}
