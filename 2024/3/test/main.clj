(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(def sample-part-one
  "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

(def sample-part-two
  "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")

(deftest test-part-one
  (testing "part-one"
    (is (= 161 (calc/part-one sample-part-one)))))

(deftest test-part-two
  (testing "part-two"
    (is (= 48 (calc/part-two sample-part-two)))))

(run-tests)
