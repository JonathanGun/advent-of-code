(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(deftest test-is-monotonic-array
  (testing "success"
    (is (= true (calc/is-monotonic-array [1 2 3 4 5])))
    (is (= true (calc/is-monotonic-array [5 4 3 2 1])))
    (is (= true (calc/is-monotonic-array [1 1 1 1 1])))
    (is (= true (calc/is-monotonic-array [1 2 3 3 4])))
    (is (= true (calc/is-monotonic-array [4 3 3 2 1])))
    (is (= true (calc/is-monotonic-array [1 3 7 9 10])))
    (is (= true (calc/is-monotonic-array [10 9 7 3 1]))))

  (testing "failure"
    (is (= false (calc/is-monotonic-array [1 3 2 4 5])))
    (is (= false (calc/is-monotonic-array [5 4 3 2 3])))))

(deftest test-is-all-elements-between
  (testing "below threshold"
    (is (= false (calc/is-all-elements-diff-between [1 1 1 1 1] 1 2)))
    (is (= false (calc/is-all-elements-diff-between [1 2 3 4 5] 2 3)))
    (is (= false (calc/is-all-elements-diff-between [1 5 6 7 9] 10 20))))

  (testing "above threshold"
    (is (= false (calc/is-all-elements-diff-between [1 2 3 4 5] 0 0)))
    (is (= false (calc/is-all-elements-diff-between [1 5 10] 1 3))))

  (testing "between threshold"
    (is (= true (calc/is-all-elements-diff-between [1 2 3 4 5] 1 1)))
    (is (= true (calc/is-all-elements-diff-between [1 5 10] 1 5)))
    (is (= true (calc/is-all-elements-diff-between [1 5 10] 4 5)))))

(def sample-input [[7 6 4 2 1]
                   [1 2 7 8 9]
                   [9 7 6 2 1]
                   [1 3 2 4 5]
                   [8 6 4 4 1]
                   [1 3 6 7 9]])

(deftest test-part-one
  (testing "sample.in"
    (is (= 2 (calc/part-one sample-input)))))

(deftest test-part-two
  (testing "sample.in"
    (is (= 4 (calc/part-two sample-input)))))

(run-tests)
