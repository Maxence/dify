class FileOnlyMessageConfigManager:
    @classmethod
    def convert(cls, config: dict) -> bool:
        file_only = False
        item = config.get("file_only_message")
        if item and item.get("enabled"):
            file_only = True
        return file_only

    @classmethod
    def validate_and_set_defaults(cls, config: dict) -> tuple[dict, list[str]]:
        if not config.get("file_only_message"):
            config["file_only_message"] = {"enabled": False}
        if not isinstance(config["file_only_message"], dict):
            raise ValueError("file_only_message must be of dict type")
        if "enabled" not in config["file_only_message"] or not isinstance(config["file_only_message"]["enabled"], bool):
            config["file_only_message"]["enabled"] = False
        return config, ["file_only_message"]
