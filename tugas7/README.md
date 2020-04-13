# Tugas 7
## Hasil Performance Test menggunakan server_thread_http.py
<table class="tg">
  <tr>
    <th class="tg-9wq8">No Test</th>
    <th class="tg-9wq8">Concurrency Level</th>
    <th class="tg-9wq8">Time Taken a Test (second)</th>
    <th class="tg-9wq8">Complete Request</th>
    <th class="tg-9wq8">Failed Request</th>
    <th class="tg-9wq8">Total Transferred (bytes)</th>
    <th class="tg-9wq8">Request per Second (#/sec)</th>
    <th class="tg-9wq8">Time per Request (ms)</th>
    <th class="tg-9wq8">Transfer Rate (Kbytes/sec)</th>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="3">1</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0.039</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">257.08</td>
    <td class="tg-9wq8">3.890</td>
    <td class="tg-9wq8">40.17</td>
  </tr>
  <tr>
    <td class="tg-9wq8">5</td>
    <td class="tg-9wq8">2.021</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">4.95</td>
    <td class="tg-9wq8">202.080</td>
    <td class="tg-9wq8">0.77</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">2.025</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">4.94</td>
    <td class="tg-9wq8">202.507</td>
    <td class="tg-9wq8">0.77</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="4">2</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0.882</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">56.70</td>
    <td class="tg-9wq8">17.635</td>
    <td class="tg-9wq8">8.86</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">12.121</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">4.13</td>
    <td class="tg-9wq8">242.412</td>
    <td class="tg-9wq8">0.64</td>
  </tr>
  <tr>
    <td class="tg-9wq8">30</td>
    <td class="tg-9wq8">12.105</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">4.13</td>
    <td class="tg-9wq8">242.094</td>
    <td class="tg-9wq8">0.65</td>
  </tr>
  <tr>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">12.163</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">4.11</td>
    <td class="tg-9wq8">243.267</td>
    <td class="tg-9wq8">0.64</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="4">3</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">9.718</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">10.29</td>
    <td class="tg-9wq8">97.175</td>
    <td class="tg-9wq8">1.61</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">24.753</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">4.04</td>
    <td class="tg-9wq8">247.531</td>
    <td class="tg-9wq8">0.63</td>
  </tr>
  <tr>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">24.809</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">4.03</td>
    <td class="tg-9wq8">248.095</td>
    <td class="tg-9wq8">0.63</td>
  </tr>
  <tr>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">24.855</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">4.02</td>
    <td class="tg-9wq8">248.546</td>
    <td class="tg-9wq8">0.63</td>
  </tr>
</table>

## Hasil Performance Test menggunakan server_thread_http.py
<table class="tg">
  <tr>
    <th class="tg-9wq8">No Test</th>
    <th class="tg-9wq8">Concurrency Level</th>
    <th class="tg-9wq8">Time Taken a Test (second)</th>
    <th class="tg-9wq8">Complete Request</th>
    <th class="tg-9wq8">Failed Request</th>
    <th class="tg-9wq8">Total Transferred (bytes)</th>
    <th class="tg-9wq8">Request per Second (#/sec)</th>
    <th class="tg-9wq8">Time per Request (ms)</th>
    <th class="tg-9wq8">Transfer Rate (Kbytes/sec)</th>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="3">1</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0.007</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">1434.10</td>
    <td class="tg-9wq8">0.697</td>
    <td class="tg-9wq8">224.08</td>
  </tr>
  <tr>
    <td class="tg-9wq8">5</td>
    <td class="tg-9wq8">0.005</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">2005.21</td>
    <td class="tg-9wq8">0.499</td>
    <td class="tg-9wq8">313.31</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0.009</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1600</td>
    <td class="tg-9wq8">1113.96</td>
    <td class="tg-9wq8">0.898</td>
    <td class="tg-9wq8">174.06</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="4">2</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0.029</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">1728.85</td>
    <td class="tg-9wq8">0.578</td>
    <td class="tg-9wq8">270.13</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">1.016</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">49.24</td>
    <td class="tg-9wq8">20.310</td>
    <td class="tg-9wq8">7.69</td>
  </tr>
  <tr>
    <td class="tg-9wq8">30</td>
    <td class="tg-9wq8">1.523</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">32.83</td>
    <td class="tg-9wq8">30.455</td>
    <td class="tg-9wq8">5.13</td>
  </tr>
  <tr>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">1.518</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">8000</td>
    <td class="tg-9wq8">32.93</td>
    <td class="tg-9wq8">30.368</td>
    <td class="tg-9wq8">5.15</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="4">3</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">0.070</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">1432.48</td>
    <td class="tg-9wq8">0.698</td>
    <td class="tg-9wq8">223.83</td>
  </tr>
  <tr>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">2.528</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">39.55</td>
    <td class="tg-9wq8">25.282</td>
    <td class="tg-9wq8">6.18</td>
  </tr>
  <tr>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">3.031</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">33.00</td>
    <td class="tg-9wq8">30.306</td>
    <td class="tg-9wq8">5.16</td>
  </tr>
  <tr>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">3.533</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">16000</td>
    <td class="tg-9wq8">28.30</td>
    <td class="tg-9wq8">35.330</td>
    <td class="tg-9wq8">4.42</td>
  </tr>
</table>

## Kesimpulan
Dapat dilihat dari perbandingan kedua tabel diatas Asyncronus Server memiliki performa yang lebih baik sehingga lebih cepat dibandingkan dengan Multithreaded Server
