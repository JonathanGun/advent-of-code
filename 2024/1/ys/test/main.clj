(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(deftest test-part-one
  (testing "should return the sum of the absolute differences between the sorted odd and even numbers"
    (is (= 0 (calc/part-one [1 1 2 2])))
    (is (= 2 (calc/part-one [1 2 3 4]))))
  (testing "sample case"
    (is (= 11 (calc/part-one [3 4 4 3 2 5 1 3 3 9 3 3])))))

(deftest test-part-two
  (testing "should return the sum of the products of the count of the odd numbers and the count of the corresponding even numbers"
    (is (= 3 (calc/part-two [1 1 2 2])))
    (is (= 0 (calc/part-two [1 2 3 4]))))
  (testing "sample case"
    (is (= 31 (calc/part-two [3 4 4 3 2 5 1 3 3 9 3 3])))))

(run-tests)
