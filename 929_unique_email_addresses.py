class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        hash_map = {}
        for email in emails:
            plus_pos = email.find('+')
            at_pos = email.find('@')
            email = ''.join(email[:plus_pos].split('.')) + email[at_pos:]
            hash_map[email] = True
        return len(hash_map)
