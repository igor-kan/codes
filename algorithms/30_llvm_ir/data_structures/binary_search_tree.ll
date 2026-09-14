; ModuleID = 'algorithms/02_c/data_structures/binary_search_tree.c'
source_filename = "algorithms/02_c/data_structures/binary_search_tree.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nofree nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable
define dso_local noundef ptr @insert(ptr noundef captures(address_is_null, ret: address, provenance) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = icmp eq ptr %0, null
  br i1 %3, label %4, label %7

4:                                                ; preds = %2
  %5 = tail call noalias dereferenceable_or_null(24) ptr @malloc(i64 noundef 24) #4
  store i32 %1, ptr %5, align 8, !tbaa !9
  %6 = getelementptr inbounds nuw i8, ptr %5, i64 8
  tail call void @llvm.memset.p0.i64(ptr noundef nonnull align 8 dereferenceable(16) %6, i8 0, i64 16, i1 false)
  br label %10

7:                                                ; preds = %2
  %8 = load i32, ptr %0, align 8, !tbaa !9
  %9 = icmp slt i32 %1, %8
  br i1 %9, label %12, label %16

10:                                               ; preds = %16, %4, %18, %12
  %11 = phi ptr [ %0, %18 ], [ %0, %12 ], [ %0, %16 ], [ %5, %4 ]
  ret ptr %11

12:                                               ; preds = %7
  %13 = getelementptr inbounds nuw i8, ptr %0, i64 8
  %14 = load ptr, ptr %13, align 8, !tbaa !13
  %15 = tail call ptr @insert(ptr noundef %14, i32 noundef %1)
  store ptr %15, ptr %13, align 8, !tbaa !13
  br label %10

16:                                               ; preds = %7
  %17 = icmp sgt i32 %1, %8
  br i1 %17, label %18, label %10

18:                                               ; preds = %16
  %19 = getelementptr inbounds nuw i8, ptr %0, i64 16
  %20 = load ptr, ptr %19, align 8, !tbaa !14
  %21 = tail call ptr @insert(ptr noundef %20, i32 noundef %1)
  store ptr %21, ptr %19, align 8, !tbaa !14
  br label %10
}

; Function Attrs: mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite)
declare noalias noundef ptr @malloc(i64 noundef) local_unnamed_addr #1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local noundef ptr @search(ptr noundef readonly captures(address_is_null, ret: address, provenance) %0, i32 noundef %1) local_unnamed_addr #2 {
  %3 = icmp eq ptr %0, null
  br i1 %3, label %14, label %4

4:                                                ; preds = %2, %8
  %5 = phi ptr [ %12, %8 ], [ %0, %2 ]
  %6 = load i32, ptr %5, align 8, !tbaa !9
  %7 = icmp eq i32 %6, %1
  br i1 %7, label %14, label %8

8:                                                ; preds = %4
  %9 = icmp slt i32 %1, %6
  %10 = select i1 %9, i64 8, i64 16
  %11 = getelementptr inbounds nuw i8, ptr %5, i64 %10
  %12 = load ptr, ptr %11, align 8, !tbaa !15
  %13 = icmp eq ptr %12, null
  br i1 %13, label %14, label %4

14:                                               ; preds = %4, %8, %2
  %15 = phi ptr [ null, %2 ], [ null, %8 ], [ %5, %4 ]
  ret ptr %15
}

; Function Attrs: nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #3

attributes #0 = { nofree nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree norecurse nosync nounwind sspstrong memory(read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #4 = { nounwind allocsize(0) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !6, i64 0}
!10 = !{!"BST", !6, i64 0, !11, i64 8, !11, i64 16}
!11 = !{!"p1 _ZTS3BST", !12, i64 0}
!12 = !{!"any pointer", !7, i64 0}
!13 = !{!10, !11, i64 8}
!14 = !{!10, !11, i64 16}
!15 = !{!11, !11, i64 0}
