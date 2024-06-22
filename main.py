import os
import json
from typing import Sequence

class KarabinerCombiner:
  """Combines all rules files with body to create the karabiner.json file.
  
  Attributes:
    body_path: relative path to the body.json file.
    rules_paths: relative path to each rule to be added to the body. Rules must
    follow a specific order as upstream changes in keybindings affect downstream
    new keys. Initial order is 'nav_layer', 'top_layer', 'combo_keys' and 
    'number_layer'.
    karabiner.json: karabiner file to be saved in the system to apply 
    changes.
  """
  def __init__(
    self,
    body_path: str,
    rules_directory_path: str,
    rules_ordered: Sequence[str],
  ):
    """Initializes the KarabinerCombiner class.
    
    Args:
      body_path: relative path to the body.json file.
      rules_directory_path: relative path to the folder containing the rules.
      rules_ordered: sequence of ordered rule names to be imported.
    """
    self.body_path = body_path

    self.rules_paths = [
      os.path.join(rules_directory_path, rule_name)
      for rule_name in rules_ordered
    ]

    self.karabiner_json = self.build_karabiner_json()

  def build_karabiner_json(self) -> json:
    """Loads body and rules and builds the karabiner.json file."""
    karabiner_json = self.get_body_content()
    
    for rule_path in self.rules_paths:
      with open(rule_path, "r") as rule_data:
        rule_content = json.load(rule_data)
      
      karabiner_json['profiles'][0]['complex_modifications']['rules'].append(
      rule_content
      )

    return karabiner_json

  def get_body_content(self) -> json:
    """Loads the body of the karabiner.json file."""
    with open(self.body_path, "r") as body_data:
        return json.load(body_data)

  def save_karabiner_file(self, path: str) -> None:
    """Saves the karabiner json file."""
    with open(path, "w") as karabiner_data:
      json.dump(self.karabiner_json, karabiner_data, indent=4)


def main():
  karabiner_combiner = KarabinerCombiner(
    body_path="./json_files/body/body.json",
    rules_directory_path="./json_files/rules",
    rules_ordered=[
      'nav_layer.json',
      'top_layer.json',
      'combo_keys.json',
      'number_layer.json',
    ],
  )

  # Save a karabiner backup for version control and inspection.
  karabiner_combiner.save_karabiner_file(path="./karabiner.json")

  karabiner_combiner.save_karabiner_file(
    path="/Users/danilodaraujo/.config/karabiner/karabiner.json",
  )

if __name__== "__main__":
    main()