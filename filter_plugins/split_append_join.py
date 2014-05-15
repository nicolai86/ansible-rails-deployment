class FilterModule(object):
  def filters(self):
    return {
      'split': self.split,
      'append': self.append,
      'join': self.join,
    }

  def split(self, path, separator):
    return path.split(separator)

  def append(self, array, suffix):
    return map(lambda x: x + suffix, array)

  def join(self, array, separator):
    return separator.join(array)