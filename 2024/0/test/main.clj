(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

;; (deftest test-calculate-result
;;   (testing "calculate-result"
;;     (is (= 0 (calc/calculate-result [1 1 2 2])))
;;     (is (= 2 (calc/calculate-result [1 2 3 4])))
;;     (is (= 11 (calc/calculate-result [3 4 4 3 2 5 1 3 3 9 3 3])))))

(run-tests)
