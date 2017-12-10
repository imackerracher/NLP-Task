# Baseline
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 238, 3: 92, 0: 90, 1: 16, -3: 7, -1: 3, 2: 3})

Accuracy: 0.224944320713
Accuracy for small interval: 0.445434298441
Accuracy for right direction: 0.412026726058

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.53      0.13        34
          0       0.28      0.24      0.26       105
          1       0.12      0.22      0.15        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.09      0.12      0.09       449


# Nonlin SVM

Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 449})

Accuracy: 0.233853006682
Accuracy for small interval: 0.438752783964
Accuracy for right direction: 0.233853006682

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.00      0.00      0.00        34
          0       0.23      1.00      0.38       105
          1       0.00      0.00      0.00        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.05      0.23      0.09       449


# Gaussian NB

Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 308, -2: 96, 3: 45})

Accuracy: 0.216035634744
Accuracy for small interval: 0.412026726058
Accuracy for right direction: 0.293986636971

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.06      0.18      0.09        34
          0       0.23      0.68      0.34       105
          1       0.18      0.14      0.16        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.08      0.19      0.11       449


# Multinomial NB

Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-1: 158, 2: 147, 3: 64, -3: 42, -2: 21, 1: 17})

Accuracy: 0.102449888641
Accuracy for small interval: 0.407572383073
Accuracy for right direction: 0.43429844098

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.08      0.50      0.13        34
          0       0.00      0.00      0.00       105
          1       0.14      0.55      0.22        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.02      0.11      0.04       449


# Grid Search

{'C': 0.001}
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 176, 3: 167, 0: 83, 1: 13, -3: 7, 2: 2, -1: 1})

Accuracy: 0.211581291759
Accuracy for small interval: 0.380846325167
Accuracy for right direction: 0.403118040089

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.09      0.47      0.15        34
          0       0.29      0.23      0.26       105
          1       0.16      0.50      0.24        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.09      0.15      0.10       449

# Variance Threshold

## Threshhold: 0
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 238, 3: 92, 0: 90, 1: 16, -3: 7, -1: 3, 2: 3})

Accuracy: 0.224944320713
Accuracy for small interval: 0.445434298441
Accuracy for right direction: 0.412026726058

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.53      0.13        34
          0       0.28      0.24      0.26       105
          1       0.12      0.22      0.15        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.09      0.12      0.09       449

## Threshhold: 0.01
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 248, 0: 108, 3: 53, -1: 23, 1: 9, -3: 5, 2: 3})

Accuracy: 0.207126948775
Accuracy for small interval: 0.423162583519
Accuracy for right direction: 0.369710467706

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.53      0.12        34
          0       0.23      0.24      0.23       105
          1       0.08      0.09      0.08        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.11      0.07       449

## Threshhold: 0.05
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 199, 0: 134, -1: 66, 3: 17, 1: 13, 2: 10, -3: 10})

Accuracy: 0.198218262806
Accuracy for small interval: 0.463251670379
Accuracy for right direction: 0.354120267261

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.06      0.47      0.10        34
          0       0.21      0.27      0.23       105
          1       0.15      0.10      0.12        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.11      0.08       449

## Threshhold: 0.1
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({-2: 352, -3: 55, 0: 26, 3: 9, -1: 4, 1: 3})

Accuracy: 0.189309576837
Accuracy for small interval: 0.409799554566
Accuracy for right direction: 0.403118040089

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.08      0.91      0.14        34
          0       0.12      0.03      0.05       105
          1       0.00      0.00      0.00        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.03      0.08      0.02       449

## Threshhold: 0.5
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 372, 3: 77})

Accuracy: 0.202672605791
Accuracy for small interval: 0.391982182628
Accuracy for right direction: 0.247216035635

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.00      0.00      0.00        34
          0       0.22      0.78      0.34       105
          1       0.14      0.19      0.16        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.21      0.10       449


# KBest
## k: 10
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 411, 3: 34, -2: 4})

Accuracy: 0.213808463252
Accuracy for small interval: 0.41425389755
Accuracy for right direction: 0.227171492205

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.00      0.00      0.00        34
          0       0.22      0.85      0.34       105
          1       0.06      0.03      0.04        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.06      0.20      0.09       449

## k: 50
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 400, -2: 36, 1: 7, 3: 3, 2: 2, -1: 1})

Accuracy: 0.202672605791
Accuracy for small interval: 0.405345211581
Accuracy for right direction: 0.213808463252

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.08      0.09      0.08        34
          0       0.21      0.81      0.34       105
          1       0.08      0.02      0.03        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.20      0.09       449

## k: 100
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 402, -2: 21, -1: 7, 1: 7, 3: 6, -3: 4, 2: 2})

Accuracy: 0.224944320713
Accuracy for small interval: 0.438752783964
Accuracy for right direction: 0.251670378619

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.09      0.09      0.09        34
          0       0.23      0.90      0.37       105
          1       0.13      0.03      0.05        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.08      0.22      0.10       449

## k: 200
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 335, -2: 39, -3: 28, 1: 27, 2: 11, -1: 6, 3: 3})

Accuracy: 0.202672605791
Accuracy for small interval: 0.41425389755
Accuracy for right direction: 0.244988864143

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.15      0.09        34
          0       0.22      0.71      0.34       105
          1       0.12      0.09      0.10        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.19      0.10       449

## k: 500
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 299, -2: 75, -1: 21, -3: 20, 1: 17, 2: 10, 3: 7})

Accuracy: 0.209354120267
Accuracy for small interval: 0.438752783964
Accuracy for right direction: 0.296213808463

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.09      0.29      0.13        34
          0       0.24      0.68      0.35       105
          1       0.09      0.05      0.07        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.07      0.19      0.10       449

## k: 1000
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 248, -2: 103, 2: 40, -1: 22, 1: 20, -3: 9, 3: 7})

Accuracy: 0.200445434298
Accuracy for small interval: 0.445434298441
Accuracy for right direction: 0.314031180401

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.26      0.11        34
          0       0.24      0.56      0.33       105
          1       0.13      0.16      0.14        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.08      0.17      0.10       449

## k: 5000
Real values: Counter({0: 105, -2: 95, -3: 69, 1: 58, 3: 53, 2: 35, -1: 34})
Predicted values: Counter({0: 204, -2: 119, 1: 56, -1: 33, -3: 18, 3: 13, 2: 6})

Accuracy: 0.207126948775
Accuracy for small interval: 0.427616926503
Accuracy for right direction: 0.327394209354

Classwise evaluation:
             precision    recall  f1-score   support

         -3       0.00      0.00      0.00        69
         -2       0.00      0.00      0.00        95
         -1       0.07      0.35      0.12        34
          0       0.24      0.46      0.31       105
          1       0.16      0.21      0.18        58
          2       0.00      0.00      0.00        35
          3       0.00      0.00      0.00        53

avg / total       0.08      0.16      0.10       449

