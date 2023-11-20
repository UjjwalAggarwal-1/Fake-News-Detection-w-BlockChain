import datetime
P2P_PORT = 5000
# REWARD FOR BLOCK PROPOSER WHOSE BLOCK IS ACCEPTED
BLOCK_REWARD = 5
# MINIMUM STAKE REQUIRED TO BECOME A VALIDATOR
MIN_STAKE = 30
# DEFAULT BALANCES FOR DIFFERENT USER_TYPES
DEFAULT_BALANCE = {"Reader": 40, "Auditor": 80}
# START TIME [USED BY BACKGROUN TASK TO FIND NEXT INTERVAL]
START_TIME = datetime.datetime(2009, 1, 3)
# TIME IN SECONDS BETWEEN CHOOSING VALIDATORS
BLOCK_VALIDATOR_CHOOSE_INTERVAL = 20
# MAXIMUM AMOUNT OF TRANSACTIONS IN A BLOCK
BLOCK_TRANSACTION_LIMIT = 3
# REWARD TO SENDER FOR BROADCASTING TRUE NEWS
SENDER_REWARD = 0.05
# PERCENTAGE OF BALANCE REMOVED FROM A NEWS SENDER IF HE BROADCASTS FAKE NEWS
SENDER_PENALTY_PERCENT = 0.5
# PENALTY PERCENTAGE OF STAKE FOR VOTING IN DISAGREEMENT WITH MAJORITY OVER A NEWS
PENALTY_STAKE_PERCENT = 0.5
# PENALTY FOR NOT PROPOSING A BLOCK [V. SMALL]
PENALTY_NO_BLOCK = 0.5
# should be 32 bytes long
VM_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAterLd6YYkT4IvL3Sh2DmFJaQeYAlr2tM7Ozq0LOQDPMdSyrb
JHl7UT55PWwFqIjMzMeRzuhJ6A2Z/IZCuiE9jaEjzaojQQY3j/AwEzAvEEutx0gc
XVpnhfoDnJbjXCiu17KvjXlsDJ70qYt73YXA4Bl4enfyZVRkzlBBxVdHxuZ+1yx/
fnTK27jGUD6f8rH4OrwNJatQ1rGJjMieo3+GBcld2jWE3jYQ7j6dHl5htr0MHD1Y
u3i0ANF2vuW7Z9AhtL0AyZNzLLrtH1KpiHVQWIFVFoCVgzGNkOs8sYXEkVZPrMJ1
46DO9hxXssRD+TmKoL5Byp+UV4k++QdniWAuUwIDAQABAoIBADx1pVvFmwKigFri
J5cQsEcFZ0zKNzweyDkx4DSuiOCU6BZ0TtLHgSGWRssQHK1Pkek5Jo+CihWSd6wC
nyinJYLtnC2dLwxMWaj/5apq6CldTYsevzaTdjaDyjF/wF5/suRDIa8+PJfROHUk
w2zzKBASxwTE2o2sx7f92m4QvO0wW3AVYjYzHIDcfKiv4/vIQ74htMkVfj92grmm
gkSQv9kSCRVMYhmJlejiY3iU/1i0NpOuh44nxDhYPn2Wa9sUIaXyDoLabnRbd+75
jUA7iKB82EHQQbuVFhAOrUwhMyS6opQOQT6pulKCnwW2aSFd7Jb+O773gEYGUyIF
xkA0lNkCgYEAwFaiJS8lhdtXcCHiHjO6S/z/16vUZZrQyAbPW5b/ynUv3dkS2gIc
EspfOXhguIRhZ2NO1blkJo8hg3DI71CWP13LmGeSIQ/+PD/8TkACyEMIVNSEfWyd
suULc6zMbOEVz7iGj1eURK+if7gmu6N0DqiQcsSrQeSfXKHz1LKSEBUCgYEA8iEj
9zvdpDpA/z1LHZ93Lcs3hrGzMk6XlsxHkFOJPH1WU+biekW1jhP6gwe88p+cVKXg
0/sSTZ885g+h9SaukyH/YItdrNDAovmHpcQ/gwqbZPPss9h8ljHRjDh33ICYPC0Q
PrvHm1midP/+ScBBmavRxWsc2Ec7KCOoFfu8dscCgYB/GQB+x9/oy1/FVm6gfJgv
3JiHwSFSnvI2K+HcaTTQaY3e8LH3ZAt/E0HHrVdktv3SnxoaOy8GF/ESdXYiRkNy
zh1asZ4rwPDEiZfFcaElCr63p9OBOkQfUiG2J8rSbA7Iu+wXTs1IcjNUaLEXr1Ri
11rUrEdq/JOeV9rTg8jnXQKBgCyE72n79erGU0Ea8f7GXVFsNg9sCPjM/o5ZjSb6
VRdsLD1NDINS4ej3v23sNE+gDUx7G3WeimT/TGE4qpy6ugqPi7ciqNynnWPZ4ZkX
Fl5vytarCvCec3niOxc/IrrGYjdeSchfGnpz5q0AjK7ezLEGqJFV+n3Byxy8QaGZ
IbPtAoGAItRVATZSN+ny2u+e+ATX79YWEu9243OramhjC5K+mIcEhZMGR0Zn1Bp+
MOzJN8raLpeGJsvZ3sD1SQYwFjizr2/Z1x4Xq3ySwVZWaPxVBowdF1jjVHsclknn
S5WICPezLZZk7729LGBXod+HeUXHuKSiQ2zPW4RaFwfMn/2jMVM=
-----END RSA PRIVATE KEY-----"""


VM_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAterLd6YYkT4IvL3Sh2Dm
FJaQeYAlr2tM7Ozq0LOQDPMdSyrbJHl7UT55PWwFqIjMzMeRzuhJ6A2Z/IZCuiE9
jaEjzaojQQY3j/AwEzAvEEutx0gcXVpnhfoDnJbjXCiu17KvjXlsDJ70qYt73YXA
4Bl4enfyZVRkzlBBxVdHxuZ+1yx/fnTK27jGUD6f8rH4OrwNJatQ1rGJjMieo3+G
Bcld2jWE3jYQ7j6dHl5htr0MHD1Yu3i0ANF2vuW7Z9AhtL0AyZNzLLrtH1KpiHVQ
WIFVFoCVgzGNkOs8sYXEkVZPrMJ146DO9hxXssRD+TmKoL5Byp+UV4k++QdniWAu
UwIDAQAB
-----END PUBLIC KEY-----"""
