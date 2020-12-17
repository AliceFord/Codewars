def count_smileys(arr):
    ans = 0
    for smiley in arr:
        if smiley.find(':') > -1 or smiley.find(';') > -1:
                if smiley.find(')') > -1 or smiley.find('D') > -1:
                    ans += 1
    return ans

print(count_smileys([':)',':(',':D',':O',':;']))