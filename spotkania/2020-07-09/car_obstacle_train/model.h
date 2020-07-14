#pragma once
#include <math.h>

/**
 * @brief Calculates the dot product of two float arrays
 * @param[in] float The first float array
 * @param[in] float The second float array
 * @param[in] int Number of elements in the array
 * @return float The result
 */
float dot(float v[], float u[], int n)
{
    float result = 0.0;
    for (int i = 0; i < n; i++)
        result += v[i]*u[i];
    return result;
}

float weight_1[6][3] = {{ 0.69388396, -0.18363768, -0.48691928},
        {-0.11122542,  0.09409314,  0.48345053},
        {-0.6351829 ,  0.8122994 ,  0.34991562},
        { 0.73035145, -0.2926492 , -0.09623587},
        { 0.42388558,  0.291497  , -0.6941188 },
        {-0.31986186,  0.42326367, -0.4152213 }};

float bias_1[3] = { -0.05082855,  0.        ,  0.        };

float weight_2[3][5] = {{-0.4100235 ,  0.4793676 , -0.01442659,  0.7790407 , -0.58525103},
        { 0.06853658,  0.59284264,  0.75364965, -0.42056793, -0.7062055 },
        { 0.39540118,  0.46259648, -0.2965532 , -0.85764015, -0.45471957}};

float bias_2[5] = { 0.0306683,  0.0515581,  0.0409896, -0.052255 ,  0.035845 };

void calculate_layer(float input[], float output[], float *weights, float *bias, int dim_input, int dim_output) {
  for (int i=0; i< dim_output; i++) {
      float result = 0.0;
      for(int k = 0; k < dim_input; k++) {
          result +=   input[k] * weights[k*dim_output + i];
      }
      
      output[i] = result + bias[i];
  }
  return;
}

void relu(float input[], int dim_input) {
    for (int i=0; i< dim_input; i++) {
        input[i] = (input[i] < 0) ? 0 : input[i];
    }
}

void softmax(float input[], int dim_input) {
    float maxv = input[0];
    for (int i=1; i< dim_input; i++) {
        maxv = (input[i]>maxv) ? input[i] : maxv;
    }
//    Serial.print("MAX: "); Serial.print(maxv);
    for (int i = 0; i < dim_input; i++) {
        input[i] = exp(input[i]-maxv);
    }
    float divv = 0;
    for (int i = 0; i < dim_input; i++) {
        divv += input[i];
    }
//    Serial.print(" DIV: "); Serial.print(divv);
    for (int i = 0; i < dim_input; i++) {
        input[i] = input[i]/divv;
    }
}

float layer1_output[3];
float output[5];

unsigned char decoder[5] = { '*', 'D', 'L', 'R', 'U' };


int argmax(float input[],int dim) {
  int max_i = 0;
  float max_v = input[0];
  for(int i=1;i<dim;i++) {
    if(input[i]>max_v) {
      max_i = i;
      max_v = input[i];
    }
  }
  return max_i;
}

unsigned char model_predict(float *input) {
//    Serial.println(); Serial.print("INPUT: "); 
//    for(int i=0;i<5;i++) {
//      Serial.print(input[i]); Serial.print(", "); 
//    }

    calculate_layer(input, layer1_output, &weight_1[0][0], &bias_1[0], 6, 3);
    relu(layer1_output, 3);
    calculate_layer(layer1_output,output ,&weight_2[0][0],&bias_2[0], 3, 5);

//    Serial.println(); Serial.print("MODEL: "); 
//    for(int i=0;i<5;i++) {
//      Serial.print(output[i]); Serial.print(", "); 
//    }
//    
    softmax(output,5);
//    Serial.print(" = "); Serial.print(argmax(output,5));
    return decoder[argmax(output,5)];
}
