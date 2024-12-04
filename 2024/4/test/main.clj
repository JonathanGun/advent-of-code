(ns test.main
  (:require [calc]
            [clojure.test :refer [deftest is run-tests testing]]))

(deftest test-count-xmas-in-line
  (testing "no xmas"
    (is (= 0 (calc/count-xmas-in-line "XXXX")))
    (is (= 0 (calc/count-xmas-in-line "MMMM")))
    (is (= 0 (calc/count-xmas-in-line "XMAX")))
    (is (= 0 (calc/count-xmas-in-line "XMAXMAXMAMXMXAMMXAMXAMXXAMS"))))
  (testing "one xmas"
    (is (= 1 (calc/count-xmas-in-line "XMAS")))
    (is (= 1 (calc/count-xmas-in-line "XXXXXMAS")))
    (is (= 1 (calc/count-xmas-in-line "XMASXXXX")))
    (is (= 1 (calc/count-xmas-in-line "MMXMASMM"))))
  (testing "multiple xmas"
    (is (= 2 (calc/count-xmas-in-line "XMASXMAS")))
    (is (= 3 (calc/count-xmas-in-line "XMASXMASXMAS")))
    (is (= 2 (calc/count-xmas-in-line "XMASXXXMASXMAAS"))))
  (testing "xmas and samx"
    (is (= 2 (calc/count-xmas-in-line "XMASSAMX")))
    (is (= 2 (calc/count-xmas-in-line "SAMXXMAS")))
    (is (= 2 (calc/count-xmas-in-line "SAMXMAS")))
    (is (= 2 (calc/count-xmas-in-line "XMASAMX")))
    (is (= 3 (calc/count-xmas-in-line "XMASAMXMMXAXAMSAMX")))))

(deftest rotate-90
  (let [input ["123" "456"]]
    (testing "rotate 90"
      (is (= ["41" "52" "63"] (calc/rotate-90 input)))
      (is (= ["654" "321"] (calc/rotate-90 (calc/rotate-90 input))))
      (is (= ["36" "25" "14"] (calc/rotate-90 (calc/rotate-90 (calc/rotate-90 input)))))
      (is (= input (calc/rotate-90 (calc/rotate-90 (calc/rotate-90 (calc/rotate-90 input)))))))))

(deftest rotate-45
  (let [input ["123"
               "456"
               "789"]
        input-2 ["1234"
                 "5678"
                 "9abc"
                 "defg"]]
    (testing "rotate 45"
      (is (= ["1"
              "42"
              "753"
              "86"
              "9"] (calc/rotate-45 input)))
      (is (= ["1"
              "52"
              "963"
              "da74"
              "eb8"
              "fc"
              "g"] (calc/rotate-45 input-2))))))

(def sample-input
  ["MMMSXXMASM"
   "MSAMXMSMSA"
   "AMXSXMAAMM"
   "MSAMASMSMX"
   "XMASAMXAMM"
   "XXAMMXXAMA"
   "SMSMSASXSS"
   "SAXAMASAAA"
   "MAMMMXMMMM"
   "MXMXAXMASX"])

(deftest test-part-one
  (testing "part-one"
    (is (= 18 (calc/part-one sample-input)))))

(deftest test-part-two
  (testing "part-two"
    (is (= 9 (calc/part-two sample-input)))))

(run-tests)
