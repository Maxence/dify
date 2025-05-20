class FileOnlyMessageConfigManager:
    @classmethod
    def convert(cls, config: dict) -> bool:
        """Convert model config to feature flag"""
        file_only_message = False
        flag = config.get("file_only_message")
        if flag and flag.get("enabled"):
            file_only_message = True
        return file_only_message

    @classmethod
    def validate_and_set_defaults(cls, config: dict) -> tuple[dict, list[str]]:
        """Validate and set defaults for file only message feature"""
        if not config.get("file_only_message"):
            config["file_only_message"] = {"enabled": False}

        if not isinstance(config["file_only_message"], dict):
            raise ValueError("file_only_message must be of dict type")

        if "enabled" not in config["file_only_message"] or not isinstance(config["file_only_message"]["enabled"], bool):
            config["file_only_message"]["enabled"] = False

        return config, ["file_only_message"]
