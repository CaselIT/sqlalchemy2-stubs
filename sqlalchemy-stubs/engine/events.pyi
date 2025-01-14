from typing import Any

from .base import Engine as Engine
from .interfaces import Connectable as Connectable
from .interfaces import Dialect as Dialect
from .. import event as event
from .. import exc as exc

class ConnectionEvents(event.Events):
    def before_execute(
        self,
        conn: Any,
        clauseelement: Any,
        multiparams: Any,
        params: Any,
        execution_options: Any,
    ) -> None: ...
    def after_execute(
        self,
        conn: Any,
        clauseelement: Any,
        multiparams: Any,
        params: Any,
        execution_options: Any,
        result: Any,
    ) -> None: ...
    def before_cursor_execute(
        self,
        conn: Any,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Any,
        executemany: Any,
    ) -> None: ...
    def after_cursor_execute(
        self,
        conn: Any,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Any,
        executemany: Any,
    ) -> None: ...
    def handle_error(self, exception_context: Any) -> None: ...
    def engine_connect(self, conn: Any, branch: Any) -> None: ...
    def set_connection_execution_options(
        self, conn: Any, opts: Any
    ) -> None: ...
    def set_engine_execution_options(self, engine: Any, opts: Any) -> None: ...
    def engine_disposed(self, engine: Any) -> None: ...
    def begin(self, conn: Any) -> None: ...
    def rollback(self, conn: Any) -> None: ...
    def commit(self, conn: Any) -> None: ...
    def savepoint(self, conn: Any, name: Any) -> None: ...
    def rollback_savepoint(
        self, conn: Any, name: Any, context: Any
    ) -> None: ...
    def release_savepoint(
        self, conn: Any, name: Any, context: Any
    ) -> None: ...
    def begin_twophase(self, conn: Any, xid: Any) -> None: ...
    def prepare_twophase(self, conn: Any, xid: Any) -> None: ...
    def rollback_twophase(
        self, conn: Any, xid: Any, is_prepared: Any
    ) -> None: ...
    def commit_twophase(
        self, conn: Any, xid: Any, is_prepared: Any
    ) -> None: ...

class DialectEvents(event.Events):
    def do_connect(
        self, dialect: Any, conn_rec: Any, cargs: Any, cparams: Any
    ) -> None: ...
    def do_executemany(
        self, cursor: Any, statement: Any, parameters: Any, context: Any
    ) -> None: ...
    def do_execute_no_params(
        self, cursor: Any, statement: Any, context: Any
    ) -> None: ...
    def do_execute(
        self, cursor: Any, statement: Any, parameters: Any, context: Any
    ) -> None: ...
    def do_setinputsizes(
        self,
        inputsizes: Any,
        cursor: Any,
        statement: Any,
        parameters: Any,
        context: Any,
    ) -> None: ...
