(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(def sample-rules
  [[47 53] [97 13] [97 61] [97 47] [75 29] [61 13] [75 53] [29 13] [97 29] [53 29] [61 53] [97 53] [61 29] [47 13] [75 47] [97 75] [47 61] [75 61] [47 29] [75 13] [53 13]])

(def sample-instructions
  [[75 47 61 53 29] [97 61 53 29 13] [75 29 13] [75 97 47 61 53] [61 13 29] [97 13 75 29 47]])

(deftest test-part-one
  (testing "part-one"
    (is (= 143 (calc/part-one sample-rules sample-instructions)))))

(deftest test-part-two
  (testing "part-two"
    (is (= 123 (calc/part-two sample-rules sample-instructions)))))

(run-tests)
