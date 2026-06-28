class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0

        # key (value,freq)
        self.key_to_val_freq = {}

        # freq - OrderedDict (key -> None)
        self.freq_to_keys = defaultdict(OrderedDict)

    def _update_freq(self,key):
        value, freq = self.key_to_val_freq[key]

        # Remove key from current freq list
        del self.freq_to_keys[freq][key]

        # If this freq list becomes empty
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Increase freq
        self.key_to_val_freq[key] = (value, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        value, _ = self.key_to_val_freq[key]
        self._update_freq(key)
        return value

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # Update existing key
        if key in self.key_to_val_freq:
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._update_freq(key)
            return

        # remove LFU key if cache is full
        if len(self.key_to_val_freq) >= self.capacity:
            lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[lfu_key]

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # insert new key
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1
