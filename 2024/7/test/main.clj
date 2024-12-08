(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(def sample-part-one
  "Hello, World!")

(def sample-part-two
  "Goodbye, Mars!")

(deftest test-part-one
  (testing "part-one"
    (is (= 0 (calc/part-one sample-part-one)))))

(deftest test-part-two
  (testing "part-two"
    (is (= 0 (calc/part-two sample-part-two)))))

(run-tests)
